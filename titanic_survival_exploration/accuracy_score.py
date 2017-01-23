
#!--utf-8--

def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """
    
    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred): 
        
        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    
    else:
        return "Number of predictions does not match number of outcomes!"


if __name__ == '__main__':  
	# Test the 'accuracy_score' function
	predictions = pd.Series(np.ones(5, dtype = int))
	print accuracy_score(outcomes[:5], predictions)