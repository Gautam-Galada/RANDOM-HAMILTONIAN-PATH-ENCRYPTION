# Objective

Privacy is a major concern in this booming world. Every Alice and Bob thinks of “Encryption” and “Decryption” when it comes to security. But the one question that they have in mind is, which scheme would safeguard their privacy? When it comes to pictures, a picture is worth more than thousands of words, and there indeed are thousands of pixels in a single image. After multiple trials with different schemes, permutation schemes are yet the most reliable ones in use. Hamiltonian path is one such application of permutation schemes.

What makes Hamiltonian different from other schemes is that, in other permutation schemes, we have to perform sorting operations but in Hamiltonian we don't need to perform sorting operations. This allows us to increase the efficiency as well. In this project, we have tried to implement image encryption using random Hamiltonian paths. We have deployed a Flask application for the frontend purpose and implemented the algorithm in the backend. During the process of encryption and decryption, we have tried to research various mathematical applications such as Bernoulli shift maps, chaotic systems, bit plane slicing, and Dirac's theorem which are a part of the process in general.

# Motive

Our motive is to perform encryption and decryption on digital data by building a random Hamiltonian path along the pixels of the digital data, relevant to permutation schemes. Along with Hamiltonian path arrays with gray level (1D) substitution is achieved, and ABMs are used to generate pseudo-random numbers which play a major role in the encryption process.

# Random Hamiltonian Path

As per the graph theory, a path that visits each vertex exactly once is referred to as a Hamiltonian Path. An image has pixels, these pixels are considered as vertices and the connections between them are considered to be edges. Since Dirac's theorem states that in a graph G of N vertices, if for each vertex v, the degree of v is greater than or equal to N/2, then at least one Hamiltonian path exists in that graph (G). The pixels of an image are in a similar manner where Hamiltonian path encryption can be performed. Adding randomness to the Hamiltonian path for image encryption is done by using Bernoulli’s shift maps, chaotic systems, and bit plane slicing.

![image](https://github.com/user-attachments/assets/47264722-0a56-419d-8335-b63764d37999)


## Flask Application

Flask is a framework written in Python with no requirements for a database abstraction layer, form validation, or any other components.

### UI created using Flask:

![image](https://github.com/user-attachments/assets/7740e83c-a2f0-4631-a90d-314ec888e009)


## Encryption Functionality

An image X (m x n) is received from the Flask application. This image is first converted into a grayscale image and then converted into a matrix. This matrix is sent to the encryption function. Firstly, the image goes through a bit plane decomposition process. Bit Plane Decomposition is a process of slicing the image at different planes (bit-planes) and plays an important role in image processing. An application of this technique is data compression.

After decomposing the image to bit planes, these bit planes are composed to generate a new image (2m x 2n). Then this new image is used to iterate ABM (Adjusted Bernoulli Map) for generating a pseudo-random number (r).

### Adjusted Bernoulli Map

![image](https://github.com/user-attachments/assets/2c1d4903-db6b-4495-b6e2-d49dd9e82b4a)


To generate randomness of the Hamiltonian path, chaotic maps can serve a major purpose by generating pseudo-random numbers. As per our research, 1D chaotic maps are much more compatible and less complex. In this encryption-decryption process, we use ABMs to serve the purpose where random values of α, β are used to generate chaos. Then the decomposed bit planes are merged to generate an image Y of size (m x n). Now two 1D arrays are used to generate pseudo-random numbers and are quantized using ABM. These arrays are used for swapping purposes.

Note: There are 2 swapping operations, one before merging of decomposed bit planes and one after merging.

![image](https://github.com/user-attachments/assets/192d8d5c-f44d-4afa-8640-c73ffd18b809)


These operations result in a cipher image or an encrypted image.

## Decryption Process

Multiple XOR operations are performed:
- Reversed operation of backward substitution
- Reversed operation of forward substitution

Followed by bit plane decomposition, reverse operations of generation of random Hamiltonian path, and then followed by bit plane mergence. The output of this process results in a grayscale decrypted image.

![image](https://github.com/user-attachments/assets/1e503c54-9081-4539-95a9-8ab675e17a76)

# Conclusion

A 1D modified Bernoulli map suitable for encryption systems is proposed in this project. A revolutionary image encryption algorithm was created based on the current chaotic map. The permutation process was accomplished by creating a random Hamiltonian path through multiple bit planes. The random Hamiltonian route was then extended for grey level substitution in the diffusion process. We have also tried to explore various chaotic systems along with Bernoulli shift maps.

