'''
Task 1. Write a Python function that converts a temperature from Fahrenheit to Celsius. Use `numpy.vectorize` to apply this function to an array of temperatures: `[32, 68, 100, 212, 77]`. 
   - Formula: $C = (F - 32) \times \frac{5}{9}$

'''
import numpy as np
def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0/9.0
vectorized_conversion = np.vectorize(fahrenheit_to_celsius)
temperatures_f = np.array([32, 68, 100, 212, 77])
temperatures_c = vectorized_conversion(temperatures_f)
print("Celsius temperatures:", temperatures_c)


'''Task 2. Create a custom function that takes two arguments: a number and a power. Use `numpy.vectorize` to calculate the power for each pair of numbers in two arrays: `[2, 3, 4, 5]` and `[1, 2, 3, 4]`.

'''
def power_function(base, exponent):
    return base ** exponent
vectorized_power = np.vectorize(power_function)
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
results = vectorized_power(bases, exponents)
print("Power results:", results)

'''
Task 3. Solve the system of equations using `numpy`:

$$
\begin{cases}
4x + 5y + 6z = 7 \\
3x - y + z = 4 \\
2x + y - 2z = 5
\end{cases}
$$
'''
A = np.array([[4, 5, 6],
              [3, -1, 1],
              [2, 1, -2]])
B = np.array([7, 4, 5])
solution = np.linalg.solve(A, B)
print("Solution for (x, y, z):", solution)


'''
Task 4. Given the electrical circuit equations below, solve for $I_1, I_2, I_3$ (currents in the branches):

$$
\begin{cases}
10I_1 - 2I_2 + 3I_3 = 12 \\
-2I_1 + 8I_2 - I_3 = -5 \\
3I_1 - I_2 + 6I_3 = 15
\end{cases}
$$

'''
C = np.array([[10, -2, 3],
              [-2, 8, -1],
              [3, -1, 6]])
D = np.array([12, -5, 15])
currents = np.linalg.solve(C, D)
print("Currents (I1, I2, I3):", currents)

'''


**Image Manipulation with NumPy and PIL**

Image file: `images/birds.jpg`. Your task is to perform the following image manipulations using the **NumPy** library while leveraging **PIL** for reading and saving the image.

**Instructions:**

1. **Flip the Image**:
   - Flip the image horizontally and vertically (left-to-right and up-to-down).

2. **Add Random Noise**:
   - Add random noise to the image.

3. **Brighten Channels**:
   - Increase the brightness of the channels (r.g. red channel) by a fixed value (e.g., 40). Clip the values to ensure they stay within the 0 to 255 range.

4. **Apply a Mask**:
   - Mask a rectangular region in the image (e.g., a 100x100 area in the center) by setting all pixel values in this region to black (0, 0, 0).

**Requirements:**
- Use the **PIL** module onyl to:
  - Read the image.
  - Convert numpy array to image.
  - Save the modified image back to a file.
- Perform all manipulations using NumPy functions. Avoid using image editing functions from PIL or other libraries.

'''
from PIL import Image
# Load the image
image = Image.open('images/birds.jpg')
# Convert image to numpy array
image_array = np.array(image)
# 1. Flip the Image
flipped_horizontally = np.flip(image_array, axis=1)
flipped_vertically = np.flip(image_array, axis=0)
# Save flipped images
Image.fromarray(flipped_horizontally).save('images/birds_flipped_horizontally.jpg')
Image.fromarray(flipped_vertically).save('images/birds_flipped_vertically.jpg')
# 2. Add Random Noise
noise = np.random.randint(0, 50, image_array.shape, dtype='uint8')
noisy_image = np.clip(image_array + noise, 0, 255).astype('uint8')
Image.fromarray(noisy_image).save('images/birds_noisy.jpg')
# 3. Brighten Channels (e.g., red channel)
brightened_image = image_array.copy()
brightened_image[:, :, 0] = np.clip(brightened_image[:, :, 0] + 40, 0, 255)
Image.fromarray(brightened_image).save('images/birds_brightened_red.jpg')
# 4. Apply a Mask
masked_image = image_array.copy()
height, width, _ = masked_image.shape
center_y, center_x = height // 2, width // 2
masked_image[center_y-50:center_y+50, center_x-50:center_x+50] = 0
Image.fromarray(masked_image).save('images/birds_masked.jpg')

'''
**Bonus Challenge**:
- Create a function for each manipulation (e.g., `flip_image`, `add_noise`, `brighten_channels`, `apply_mask`) to promote modularity and reusability of code.

'''
def flip_image(image_array, axis):
    return np.flip(image_array, axis=axis)
def add_noise(image_array, noise_level=50):
    noise = np.random.randint(0, noise_level, image_array.shape, dtype='uint8')
    return np.clip(image_array + noise, 0, 255).astype('uint8')
def brighten_channels(image_array, channel_index, increase_value):
    brightened_image = image_array.copy()
    brightened_image[:, :, channel_index] = np.clip(brightened_image[:, :, channel_index] + increase_value, 0, 255)
    return brightened_image
def apply_mask(image_array, top_left, bottom_right):
    masked_image = image_array.copy()
    masked_image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = 0
    return masked_image
# Example usage of the functions
flipped_image = flip_image(image_array, axis=1)
noisy_image = add_noise(image_array, noise_level=50)
brightened_image = brighten_channels(image_array, channel_index=0, increase_value=40)
masked_image = apply_mask(image_array, (center_x-50, center_y-50), (center_x+50, center_y+50))
# Save the results  
Image.fromarray(flipped_image).save('images/birds_flipped_function.jpg')
Image.fromarray(noisy_image).save('images/birds_noisy_function.jpg')
Image.fromarray(brightened_image).save('images/birds_brightened_function.jpg')
Image.fromarray(masked_image).save('images/birds_masked_function.jpg')
