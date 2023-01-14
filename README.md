# eBike Overclocker
## This project is a research only project and not designed as a way to bypass eBike speed restrictions that may exist within your country
For example within the UK eBikes can only legally provide powered assistance up to 15.5MPH and you must use your bike on private land if you wish to exceed this speed with assistance.

### Overview
I purchased an eBike which I wanted to enjoy with the benefits of full assistance on a large area of private land my brother in law owns. As such I wanted a way to allow the assistance beyond the 15.5 MPH allowed by law in the UK, but to do so in a non-invasive way so that I could easily remove or disable the modification.

My eBike is a [Decathlon 27.5+ INCH ELECTRIC MOUNTAIN BIKE E-ST 900](https://www.decathlon.co.uk/p/27-5-inch-electric-mountain-bike-e-st-900-grey/_/R-p-168875?mc=8487240&c=GREY) which determines the speed of the bike using a magnet mounted to the rear wheel and a reed sensor. My hyposthosis was that by attaching my own reed sensor to sense the turning of the wheel this input could be interepted by a Raspberry Pi Pico that would in turn send a signal to an electromagic mounted on top of the eBikes reed sensor. 

![eBike overclocker proof of concept](https://img.youtube.com/vi/J6ejlkNBZDI/0.jpg)

[Watch proof of concept video on YouTube](https://youtu.be/J6ejlkNBZDI)


## Parts list
- [Raspberry Pi Pico](https://thepihut.com/products/raspberry-pi-pico) £4
- [Single Channel Relay for Raspberry Pi Pico](https://thepihut.com/products/single-channel-relay-for-raspberry-pi-pico) £10
- [5 volt waterproof electromagic](https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=5v+waterproof+electromagnet&_sacat=0&LH_TitleDesc=0&_odkw=5v+waterproof+electromagic&_osacat=0) £6
- Reed sensor £5
- [Milliput](https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2334524.m570.l1311&_nkw=milliput&_sacat=0&LH_TitleDesc=0&_odkw=usb+power+switch&_osacat=0&LH_PrefLoc=2)
- [Power bank keep alive](https://store.eplop.co.uk/product/smd-keepalive/) £7
- USB power bank £20 _(Optional: Your bike may have USB power output)_
- [Saddle bag](https://www.wiggle.co.uk/dhb-medium-saddle-bag-1) £9
- [USB power switch](https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=usb+power+switch&_sacat=0&LH_TitleDesc=0&_odkw=ebay+usb+switch&_osacat=0&LH_PrefLoc=20) £4 _(Optional, but recomended: Allows an easy way to turning the Pico on and off)_
- [Connectors](https://www.ebay.co.uk/itm/401536214100?hash=item5d7d6c6454:g:QIEAAOSwFV1bELpI&amdata=enc%3AAQAHAAAA8AruczEiSR6jTTRr5s%2Bddx5jHJAn3muUOEA6pracznbxKVcGb0BOIMxDr975aYSrF5k07JTOHGyVRUFdWZsXfxJ%2FyQv9m6WhpLK%2BLux6%2FRegCt8eL09ClEmYCdsBc4fBB4BORqNfD0pQCEIpJH3lNyZ5BM4I%2FwCMpwd39dkdu17y8O5aNiXxIAlZc25xP1maabRq%2FMOXiflfrHloTEeSnAdqkGPTG0PK2l5sZZ7I8D4ZrUz%2BjGN5D8RnxydYMggclCaHjGVyUxNPuOyDvQ3Euh0Qoo%2BUdl7k6L34SpRJCRTdVAr0x%2Fd6oU8CZndn9yPGAA%3D%3D%7Ctkp%3ABFBM3rfPmbZh) _(Optional, but recommended: Allows a way of easily disconnecting the sensor and electromagnet on the bike from the Pi Pico)_


## Tools and misc parts
- USB power cable for Pi Pico
- Solidering iron & solider
- Cabling (For connecting electronics together)
- Shrink wrap (To cover solidered wire connections)

## Installation
The eBike Overclocker is designed to work on bikes that have an easily accessible reed sensor that is used by the bike to determine it's current speed. By attaching an electromagic to this reed sensor the eBike overclocker can override the signals that would overwise be picked up to fool the bike into thinking it's going a speed slower than 15.5 MPH so that assistance will still be provided

### Raspberry Pi Pico
1. Install the latest MicroPython firmware on your Pico
2. Copy the code from [main.py](main.py) to your Pico
3. Attach the Relay to your Pico

At this point you should be able to power on your Pico and repeatidly bridge the connections between pins 6 and ground to simulate the input that a reed sensor would pickup from a turning wheel. This should in turn cause the relay to repeatidly trigger once a second or so.

### Reed sensor
This needs to be attached to your bike frame so that it's able to pickup the magnetic field from the magnet attached to the bike as the wheel spins. If the magnet on the bike is too weak to be detected I would recommend buying an neodymium magnet and attaching it to the wheel. These can be purchased with a hole in the magnet (think doughnut) that allows easier mounted to the wheel spokes by looping a piece of wire through the hole and round a spoke. The magnet can then be coated in Milliput putty to hold it in place.

Once mounted to the frame a cable needs to be installed running from the reed sensor and connected to pins 6 and ground on the Pico

### Electromagnet
The electromagnet needs to be mounted on or near the bikes reed sensor so that the Pico and trigger a pulse that will be picked up successfully. I would recommend using Milliput putty to help mount the electromagnet to the bike frame and to increase the weatherproofing of it.

Once mounted to the frame a cable needs to be installed running from the electromagnet to the Pico mounted relay and into a 5v USB power source. 

### Testing
I would recommend testing each component in isolation as they are being installed to ensure they work as expecting, by using a multimeter and other tools. In theory once all the components are successfully installed they should work together to override the default sensor system of the bike so that it thinks it's going a different speed than it actually is. 
