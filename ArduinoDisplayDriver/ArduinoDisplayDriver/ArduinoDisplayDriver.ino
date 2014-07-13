#include <Adafruit_NeoPixel.h>

#define TEST_SEED 1000

const uint32_t displayHeight = 22;
const uint32_t displayWidth = 10;
const uint32_t blockSize = 1;

const int numPixelsInBlock = blockSize * blockSize;
int pixelsInBlock[numPixelsInBlock];

#define PIN 6
int numPixels = 220;

// Parameter 1 = number of pixels in strip
// Parameter 2 = Arduino pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(numPixels, PIN, NEO_GRB + NEO_KHZ800);

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.

void setup() {
	strip.begin();
	strip.show(); // Initialize all pixels to 'off'
	Serial.begin(115200);
}

void loop() {

	if(Serial.available() && Serial.peek() == '!')
	{
		Serial.println("serial data available");
		Serial.read(); //get rid of the start bit
		int x,y,R,G,B;  
		int pixel;
		ClearBoard(false);
		char peek = Serial.peek();
		Serial.print("peek before:");
		Serial.println(peek);
		
		while(peek != '\n')
		{
			x = Serial.parseInt();
			y = Serial.parseInt();
			R = Serial.parseInt();
			G = Serial.parseInt();
			B = Serial.parseInt();

			Serial.println(x);
			Serial.println(y);
			Serial.println(R);
			Serial.println(G);
			Serial.println(B);

			if(x == 0 && y == 0 && & R == 0 && G == 0 && B == 0)
			{
				Serial.println("Reset to start bit");
				delay(500);
				break; //probably bad data in the queue

			}

			findPixels(x,y);

			for(int i = 0; i < numPixelsInBlock; i++)
			{
				if(pixelsInBlock[i] == -1)
				{
					Serial.println("Pixel out of range");
				}
				else
				{
					Serial.print("Lighting pixel ");
					Serial.println(pixelsInBlock[i]);
					strip.setPixelColor(pixelsInBlock[i], R,G,B); 
				}
			}

			if(Serial.available())
			{
				peek = Serial.peek();
                                if(peek = ' ' && Serial.peek() == '\n')
                                {
                                  Serial.println("space \\n"); 
                                  break; 
                                }
			}
			else
			{
				break;
			}
		}
		//clear out the newline
		Serial.println("found the stop bit");
		strip.show();
	}
	else if (Serial.available())
	{ 
		Serial.print("ignoring: ");
		Serial.println(Serial.read());//we don't care if it's not the start bit
	}
	delay(100);
}


void ClearBoard(boolean latch){
	for(int i = 0; i < numPixels; i++)
	{
		strip.setPixelColor(i, 0,0,0);   
		if(latch)
		{
			strip.show();
		}
	}
}

// Find pixels contained within a Block and populates pixelsInBlock of size blockSize^2 containing individual pixel numbers
// If a pixel number is -1, it is not in the block
// NOTE: Will return value outside of range, no bounds checking
void findPixels (int blockX, int blockY)
{
	int pixelRow, pixelCol;

	for(pixelRow = 0; pixelRow < blockSize; pixelRow++)
	{
		for(pixelCol = 0; pixelCol < blockSize; pixelCol++)
		{
			// Calculate pixel's X and Y value
			int pixelX = pixelCol + blockX * blockSize;
			int pixelY = pixelRow + blockY * blockSize;
			int index = pixelCol + blockSize * pixelRow;

			if(pixelX > displayWidth || pixelY > displayHeight)
			{
				pixelsInBlock[index] = -1;
			}
			else
			{
				pixelsInBlock[index] = pixelX + pixelY * displayWidth;
			}
		}
	}
}


