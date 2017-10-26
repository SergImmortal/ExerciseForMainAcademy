import argparse
import shutil
import os
import sys
import platform
import datetime
import inspect
def write_log(arg):
	with open('log.log', 'a') as f:
		now = datetime.datetime.now()
		f.write('==>> start action <<==\nTime: '+str(now)+ '\n' + str(arg) + '\n=====>> close <<====== \n \n')
		return

def print_stat():
    st = shutil.disk_usage(os.getcwd())
    res = "For logic disk - {} : \n Total space - {} \n Used space - {} \n Free space - {}".format(os.getcwd()[0], st.total, st.used, st.free)
    print(res)
    return write_log('Call name is "{}" \nOunput: \n{}'.format(inspect.stack()[0][3], res) )


def print_dir(arg):
	res = '\n'.join(('->> ' + i) for i in os.listdir(arg))
	print(res)
	return write_log('Call name is "{}" with argument: "{}" \nOunput: \n{}'.format(inspect.stack()[0][3], arg, res))


def print_tree(arg):
    levl2 = []
    for root, dirs, files in os.walk(arg):
        level = root.replace(arg, '').count(os.sep)
        indent = ' ' * 4 * (level)
        levl1 = '{}{}/'.format(indent, os.path.basename(root))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            levl2.append('{}{}'.format(subindent, f))
    res = levl1 +'\n'+ '\n'.join(i for i in levl2)
    print(res)
    return write_log('Call name is "{}" with argument: "{}" \nOunput: \n{}'.format(inspect.stack()[0][3], arg, res))

def print_info():
	res = 'CPU: ' + platform.processor()+ '\n OS: ' + platform.platform()
	print(res)
	return write_log('Call name is "{}" \nounput: \n{}'.format(inspect.stack()[0][3], res) )


if __name__ == '__main__':
	try:
		parser = argparse.ArgumentParser(description = 'Some ap for Main Academy')
		parser.add_argument('--action', help = "Some action")
		parser.add_argument('--path', default='0', help = "Some path")
		args = parser.parse_args() 
		param = args.path
		f = globals()[args.action]

		if param != '0':
			f(param)
		else:
			f()
	except Exception:
		error = sys.exc_info()[0].__name__+'\nCall method: '+args.action+'\nArguments: '+ args.path
		print(error)
		write_log(error)