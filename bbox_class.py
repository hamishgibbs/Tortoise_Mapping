#Define a Bounding Boxes class to store all calculations and methods for plotting
class Bounding_Boxes:

  #Instantiate Bounding_Boxes class using vector data - this class is written specifically to accept volcano specific data
  def __init__(self, vector_data):
    
    #Add vector_data attribute to inspect original vector data
    self.vector_data = vector_data
  
    #Add volcano_names class to inspect all unique volcano names (useful for plotting)
    volcano_names = list(vector_data.Name.unique())
    self.volcano_names = volcano_names
    
    #Add bboxes attribute to store bounding boxes around each volcano
    bbox = {}
    #Create one bounding box for the entire archipelago
    bbox['Archipelago'] = vector_data.total_bounds
    #Create bounding box for each island
    for island in volcano_names:
      bbox[island] = vector_data[vector_data['Name']==island].envelope
    self.bboxes = bbox
  
  #Define a method to create matplotlib compatible xlim
  def x_lim_island(self, island, zoom_factor=0.15):
    
    #Define the factor by which to zoom out x axis (this could be made into two zooms L & R)
    #z_factor = 0.15 means that 15% of the total boundign box will be added to both sides
    #This scales with the size of the island to add a border to all plots
    z_factor = zoom_factor
    
    #Archipelago is a ndarray data type not a Shapely Polygon
    if island == 'Archipelago':
      xmin = self.bboxes[island][0]
      xmax = self.bboxes[island][2]
    
      zoom = (xmax - xmin) * z_factor
      
      #Returns xlim ready for the plt.xlim function
      return(xmin - zoom, xmax + zoom)
    
    #Extract coordinates from Shapely Polygon bounding boxes
    else:
      xmin = mapping(self.bboxes[island])['bbox'][0]
      xmax = mapping(self.bboxes[island])['bbox'][2]
  
      zoom = (xmax - xmin) * z_factor
    
      #Returns xlim ready for the plt.xlim function    
      return(xmin - zoom, xmax + zoom)

  #Copy of x_lim_island for the y axis
  def y_lim_island(self, island, zoom_factor=0.15):
  
    z_factor = zoom_factor
  
    if island == 'Archipelago':
      ymin = self.bboxes[island][1]
      ymax = self.bboxes[island][3]
    
      zoom = (ymax - ymin) * z_factor
      
      return(ymin - zoom, ymax + zoom)
  
    else:
      ymin = mapping(self.bboxes[island])['bbox'][1]
      ymax = mapping(self.bboxes[island])['bbox'][3]
    
      zoom = (ymax - ymin) * z_factor
  
      return(ymin - zoom, ymax + zoom) 
