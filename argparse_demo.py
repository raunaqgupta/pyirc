
import argparse

def main(args):

	print args.log
	

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description="Sample argparse demo")
	parser.add_argument('--log', default='OFF')
	
	args = parser.parse_args()
	main(args)
