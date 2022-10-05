from transformers import pipeline
import argparse
from  typing import Union


def predict(comment='I feel that today is a beautiful day'):
    sentiment_model = pipeline("sentiment-analysis")
    pred = sentiment_model(comment)
    print('prediction for: "{}"'.format(comment))

    return pred



"""
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Predict')
	default_comment = "I felt good"
	#default_comment = '["I felt good"]'
	parser.add_argument('--comment', type=str, default=default_comment)

	
	# this part is for dealing with a list of comments
	#parser.add_argument('--comment', type=Union[str,list], default=default_comment)
	
	
	args = parser.parse_args()
	print(' we are in main: args.comment', args.comment)
	output = convert(predict(args.comment))
	print('we are in main')
	print(output)
	print('output', type(output))
	print('default_comment',type(predict(default_comment)))
	print('prediction ', predict(default_comment))
	print('1,23', type([1,2,3]))
"""


