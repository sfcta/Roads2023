MODELYEAR = None  

# --------------------------------------------------------------------------

def desc():
    return """
    Fall 2023 Bay Area road network
    """
    
def year():
    return 2023
    
def prereqs():
    return []
    
def coreqs():
    return []

def conflicts():
    return []

# --------------------------------------------------------------------------

def champVersion():
    return (4.3, None)

def wranglerVersion():
    return (2.0, None)
    
def networks():
    return ['hwy']

# --------------------------------------------------------------------------

# Don't edit these:
def apply(net, **kwargs): 
    applyFiles(net); 
    applyEdits(net)
    
def applyFiles(net): 
    pass
    
# --------------------------------------------------------------------------
def applyEdits(net):
    pass
