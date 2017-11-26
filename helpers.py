from IPython.display import Markdown, display
import pandas as pd

def print_bold(text):
	display(Markdown("**{}**".format(text)))


def display_confusion_matrix(target_test, target_predict):
	y_actu = pd.Series(target_test, name='Actual')
	y_pred = pd.Series(target_predict, name='Predicted')
	print(target_test)
	print(target_predict)
	ddsxsx
	# return pd.crosstab(y_actu, y_pred)sxsx