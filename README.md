# PixelatedCanvas.py 🎨🖌️

[![Python Version](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![Pillow Version](https://img.shields.io/badge/pillow-9.5.0-yellow)](https://pillow.readthedocs.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

**PixelatedCanvas.py** is my Python pet-project that generates stunning pixel backgrounds using various rules and sizes. It's like having a virtual art studio where you can unleash your creativity and create mesmerizing pixel masterpieces! 🎉✨

## Features

- 🌈 Generate pixel backgrounds with different rules and sizes
- 🎨 Customize the number of images to generate
- 📊 Specify the desired size of the generated images
- 🖼️ Save the generated images in the `output` directory
- 🎥 Create GIFs from the generated images using `gif_script.py`
- 🌟 Easy-to-use graphical user interface (GUI) for seamless interaction

## Installation

1. Clone the repository:
  - `git clone https://github.com/your-username/PixelatedCanvas.py.git`
2. Install the required dependencies:
  - `pip install -r requirements.txt`

## Usage

1. Run the `gui.py` script:
  - `python gui.py`
2. Select the desired rule, size, and number of images to generate using the GUI.
3. Click the "Generate Images" button to start the image generation process.
4. The generated images will be saved in the `output` directory.
5. To create a GIF from the generated images, run the `gif_script.py` script:
  - `python gif_script.py`
  - The resulting GIF will be saved in the `gifs` directory.
6. Alternatively, you can manually run script.py by uncommenting the last part of the code and specifying different settings:
  - Open `script.py` in a text editor.
  - Uncomment the last part of the code (e.g., remove the # symbols).
  - Run the last `for` look with your desired settings, such as the number of images, width, height, and rule index.
  - Save the changes and run `script.py` directly:
           ` python script.py`. This allows you to generate a large number of images in a batch, for example, generating 1,000,000 images in a row with specific sizes and rules.

Note: Be cautious when generating a large number of images, as it may take a considerable amount of time and consume significant system resources but on average one image betwen 10-30 kB at max.

Note: GIF generation using gif_script.py can take a long time, especially for a large number of images. If you encounter issues or find the process too time-consuming, you can alternatively use different scripts or websites for GIF creation, such as https://ezgif.com/maker, which provides an online tool for creating GIFs from a set of images with multiple settings.

## Showcase

Here are some examples of the pixel backgrounds generated by PixelatedCanvas.py:

### Rule 1: Cosmic Explosion 💥🌌

<img src="Showcase/1_1822_16x16_1.png" width="19%" /> <img src="Showcase/1_2397_16x16_1.png" width="19%" />  <img src="Showcase/1_3081_16x16_1.png" width="19%" /> 
<img src="Showcase/1_4205_16x16_1.png" width="19%" /> <img src="Showcase/1_4348_16x16_1.png" width="19%" />

<img src="Showcase/1_4348_16x16_1.png" width="19%" /> <img src="Showcase/1_7835_16x16_1.png" width="19%" />  <img src="Showcase/2584_16x16_1.png" width="19%" /> 
<img src="Showcase/3744_16x16_1.png" width="19%" /> <img src="Showcase/8483_16x16_1.png" width="19%" />

<img src="Showcase/1_8860_31x17_1.png" width="100%" />

<img src="Showcase/31x17_rule1.gif" width="100%" />

<img src="Showcase/1_9824_62x34_1.png" width="100%" />

<img src="Showcase/1_4238_93x51_1.png" width="100%" />

<img src="Showcase/1_5083_124x68_1.png" width="100%" />

### Rule 2: Retro Vibes 🕹️📼

<img src="Showcase/1_1148_16x16_1.png" width="19%" /> <img src="Showcase/1_2063_16x16_1.png" width="19%" />  <img src="Showcase/1_2308_16x16_1.png" width="19%" /> 
<img src="Showcase/1_2994_16x16_1.png" width="19%" /> <img src="Showcase/1_3808_16x16_1.png" width="19%" />

<img src="Showcase/1_4098_16x16_1.png" width="19%" /> <img src="Showcase/1_8316_16x16_1.png" width="19%" />  <img src="Showcase/1_9059_16x16_1.png" width="19%" /> 
<img src="Showcase/1_9891_16x16_1.png" width="19%" /> <img src="Showcase/1_6535_16x16_1.png" width="19%" />

<img src="Showcase/1_4472_31x17_1.png" width="100%" />

<img src="Showcase/31x17_rule2.gif" width="100%" />

<img src="Showcase/1_2047_62x34_1.png" width="100%" />

<img src="Showcase/1_8132_93x51_1.png" width="100%" />

<img src="Showcase/1_6080_124x68_1.png" width="100%" />


### Rule 3: Neon Dreams 🌃🌠

<img src="Showcase/3_1269_16x16_1.png" width="19%" /> <img src="Showcase/3_2158_16x16_1.png" width="19%" />  <img src="Showcase/3_2891_16x16_1.png" width="19%" /> 
<img src="Showcase/3_3441_16x16_1.png" width="19%" /> <img src="Showcase/3_3511_16x16_1.png" width="19%" />

<img src="Showcase/3_8513_16x16_1.png" width="19%" /> <img src="Showcase/3_8585_16x16_1.png" width="19%" />  <img src="Showcase/3_9317_16x16_1.png" width="19%" /> 
<img src="Showcase/3_9406_16x16_1.png" width="19%" /> <img src="Showcase/3_9852_16x16_1.png" width="19%" />

<img src="Showcase/3_4493_31x17_1.png" width="100%" />

<img src="Showcase/31x17_rule3.gif" width="100%" />

<img src="Showcase/3_8399_62x34_1.png" width="100%" />

<img src="Showcase/3_4662_93x51_1.png" width="100%" />

<img src="Showcase/3_8228_124x68_1.png" width="100%" />

### Rule 4: Pixelated Serenity 🍃🌿

<img src="Showcase/4_1428_16x16_1.png" width="19%" /> <img src="Showcase/4_2191_16x16_1.png" width="19%" />  <img src="Showcase/4_2466_16x16_1.png" width="19%" /> 
<img src="Showcase/4_2695_16x16_1.png" width="19%" /> <img src="Showcase/4_2707_16x16_1.png" width="19%" />

<img src="Showcase/4_331_16x16_1.png" width="19%" /> <img src="Showcase/4_4370_16x16_1.png" width="19%" />  <img src="Showcase/4_6764_16x16_1.png" width="19%" /> 
<img src="Showcase/4_8227_16x16_1.png" width="19%" /> <img src="Showcase/4_8251_16x16_1.png" width="19%" />

<img src="Showcase/4_8402_31x17_1.png" width="100%" />

<img src="Showcase/31x17_rule4.gif" width="100%" />

<img src="Showcase/4_6177_62x34_1.png" width="100%" />

<img src="Showcase/4_2768_93x51_1.png" width="100%" />

<img src="Showcase/4_463_124x68_1.png" width="100%" />

### Rule 5: Electric Chaos ⚡🎇

<img src="Showcase/5_1243_16x16_1.png" width="19%" /> <img src="Showcase/5_1921_16x16_1.png" width="19%" />  <img src="Showcase/5_3671_16x16_1.png" width="19%" /> 
<img src="Showcase/5_3687_16x16_1.png" width="19%" /> <img src="Showcase/5_5377_16x16_1.png" width="19%" />

<img src="Showcase/5_5757_16x16_1.png" width="19%" /> <img src="Showcase/5_6002_16x16_1.png" width="19%" />  <img src="Showcase/5_7667_16x16_1.png" width="19%" /> 
<img src="Showcase/5_8600_16x16_1.png" width="19%" /> <img src="Showcase/5_9524_16x16_1.png" width="19%" />

<img src="Showcase/5_7750_31x17_1.png" width="100%" />

<img src="Showcase/31x17_rule5.gif" width="100%" />

<img src="Showcase/5_7886_62x34_1.png" width="100%" />

<img src="Showcase/5_1117_93x51_1.png" width="100%" />

<img src="Showcase/5_8411_124x68_1.png" width="100%" />

### Rule 6: Monochromatic Elegance 🖌️🎨

<img src="Showcase/6_1805_16x16_1.png" width="19%" /> <img src="Showcase/6_2126_16x16_1.png" width="19%" />  <img src="Showcase/6_2722_16x16_1.png" width="19%" /> 
<img src="Showcase/6_3728_16x16_1.png" width="19%" /> <img src="Showcase/6_44_16x16_1.png" width="19%" />

<img src="Showcase/6_830_16x16_1.png" width="19%" /> <img src="Showcase/6_8485_16x16_1.png" width="19%" />  <img src="Showcase/6_8705_16x16_1.png" width="19%" /> 
<img src="Showcase/6_8822_16x16_1.png" width="19%" /> <img src="Showcase/6_9400_16x16_1.png" width="19%" />

<img src="Showcase/6_7532_31x17_1.png" width="100%" />

<img src="Showcase/31x17_rule6.gif" width="100%" />

<img src="Showcase/6_3765_62x34_1.png" width="100%" />

<img src="Showcase/6_7448_93x51_1.png" width="100%" />

<img src="Showcase/6_2119_124x68_1.png" width="100%" />

### Rule 7: Geometric Harmony 📐🔷

<img src="Showcase/6_1780_16x16_1.png" width="19%" /> <img src="Showcase/6_1857_16x16_1.png" width="19%" />  <img src="Showcase/6_2442_16x16_1.png" width="19%" /> 
<img src="Showcase/6_4165_16x16_1.png" width="19%" /> <img src="Showcase/6_4333_16x16_1.png" width="19%" />

<img src="Showcase/6_4884_16x16_1.png" width="19%" /> <img src="Showcase/6_7004_16x16_1.png" width="19%" />  <img src="Showcase/6_7658_16x16_1.png" width="19%" /> 
<img src="Showcase/6_9238_16x16_1.png" width="19%" /> <img src="Showcase/6_9653_16x16_1.png" width="19%" />

<img src="Showcase/6_5681_31x17_1.png" width="100%" />

<img src="Showcase/31x17_rule7.gif" width="100%" />

<img src="Showcase/6_3563_62x34_1.png" width="100%" />

<img src="Showcase/6_456_93x51_1.png" width="100%" />

<img src="Showcase/6_8560_124x68_1.png" width="100%" />

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, please open an issue or submit a pull request. Let's make PixelatedCanvas.py even more awesome together! 🤝💡

## License

This project is licensed under the MIT License.

## Acknowledgements

- The project uses the Pillow library for image manipulation.
- The GUI is built using the Tkinter library.

## Let's Create Pixel Magic! 🎨✨

Grab your virtual paintbrush and let PixelatedCanvas.py be your guide to creating stunning pixel backgrounds! Explore different rules, customize sizes, and let your creativity run wild! 🌈🎉

Happy pixel art creation! 🎨🖌️
