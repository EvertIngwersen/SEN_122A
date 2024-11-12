import biogeme.biogeme as bio
from biogeme import models
from biogeme.expressions import log


# This function estimates the MNL model and returns the estimation results
# input values: utilities for all three alternatives, the choices, the database, and the model name

def estimate_mnl(V1,V2,V3,CHOICE,database,name):
    
    # Create a dictionary to list the utility functions with the numbering of alternatives
    V = {1: V1, 2: V2, 3: V3}
        
    # Create a dictionary called av to describe the availability conditions of each alternative, where 1 indicates that the alternative is available, and 0 indicates that the alternative is not available.
    # This shows that all alternatives were available to all respondents. 
    av = {1: 1, 2: 1, 3: 1} 

    # Define the choice model: The function models.logit() computes the MNL choice probabilities of the chosen alternative given the V. 
    prob = models.logit(V, av, CHOICE)

    # Define the log-likelihood   
    LL = log(prob)
   
    # Create the Biogeme object containing the object database and the formula for the contribution to the log-likelihood of each row using the following syntax:
    biogeme = bio.BIOGEME(database, LL)
    
    # The following syntax passes the name of the model:
    biogeme.modelName = name

    # Some object settings regaridng whether to save the results and outputs 
    biogeme.generate_pickle = False
    biogeme.generate_html = False
    biogeme.save_iterations = False

    # Syntax to calculate the null log-likelihood. The null-log-likelihood is used to compute the rho-square 
    biogeme.calculateNullLoglikelihood(av)

    # This line starts the estimation and returns the results object.
    results = biogeme.estimate()
     
    return results