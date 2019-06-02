import yaml 


def get_grid_info(grid_name):
    
    """Return Grid information
    
    Parameters
    ----------
    grid_name : str
      Name of grid (i.e., POP_gx3v7, POP_gx1v7, POP_tx0.1v3)
    
    Returns
    -------
    Grid information : str 
    
    """
    
    with open('pop_grid_definitions.yaml') as f:
        grid_defs = yaml.safe_load(f)

    if grid_name not in grid_defs:
        raise ValueError(
            f"""Unknown grid: {grid_name}
             Please select from the following: {list(grid_defs.keys())}"""
        )
        
    
    return grid_defs[grid_name]