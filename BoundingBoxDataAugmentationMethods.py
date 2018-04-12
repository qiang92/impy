"""
package: Images2Dataset
class: DataAugmentationMethods
Author: Rodrigo Loza
Description: Data augmentation methods used for bounding box 
labels.
"""
# Libraries
from interface import Interface

class BoundingBoxDataAugmentationMethods(Interface):
	
	
	def jitterBoxes(self, frame = None, quantity = None):
		"""
		Creates random jitter boxes inside a bounding box cropped from its image.
		Args:
			frame: A tensor that contains an image.
			quantity: An int that tells how many jitter boxes to create inside 
							the frame.
		Returns:
			A tensor that contains an image altered by jitter boxes.
		"""
		pass

	def horizontalFlip(self, frame = None):
		"""
		Flip a bouding box by its horizontal axis.
		Args:
			frame: A tensor that contains a cropped bouding box from its frame.
		Returns:
			A tensor that has been flipped by its horizontal axis.
		"""
		pass

	def verticalFlip(self, frame = None):
		"""
		Flip a bouding box by its vertical axis.
		Args:
			frame: A tensor that contains a cropped bouding box from its frame.
		Returns:
			A tensor that has been flipped by its vertical axis.
		"""
		pass

	def randomRotation(self, frame = None, bndbox = None, theta = None):
		"""
		Rotate a frame clockwise by random degrees. Random degrees
		is a number that is between 20-360.
		Args:
			frame: A tensor that contains an image.
		Returns:
			A tensor with a rotation of the original image.
		"""
		pass

	def addRandomBlur(self, frame = None, sigma = None):
		"""
		Blur an image applying a gaussian filter with a random sigma(0, sigma_max)
		Sigma might be between 1 and 3.
		Args:
			frame: A tensor that contains an image.
		Returns:
			A tensor with a rotation of the original image.
		"""
		pass

	def shiftColors(self, frame = None):
		"""
		Shifts the colors of the frame.
		Args:
			frame: A tensor that contains an image.
		Returns:
			A tensor that has shifted the order of its colors.
		"""
		pass

	def fancyPCA(self, frame = None):
		"""
		Fancy PCA implementation.
		Args:
			frame: A tensor that contains an image.
		Returns:
			A tensor that contains the altered image by fancy PCA.
		"""
		pass
