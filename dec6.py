Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from collections import Counter
sentence = "the cat sat on the mat with the rat cat and rat were playing in the mat and the cat was happy with rat on the mat"
print(dict(Ccounter(sentence)))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(dict(Ccounter(sentence)))
NameError: name 'Ccounter' is not defined. Did you mean: 'Counter'?
print(dict(Counter(sentence)))
{'t': 18, 'h': 9, 'e': 8, ' ': 26, 'c': 3, 'a': 15, 's': 2, 'o': 2, 'n': 6, 'm': 3, 'w': 4, 'i': 4, 'r': 4, 'd': 2, 'p': 3, 'l': 1, 'y': 2, 'g': 1}
from datetime import datetime
import time
SyntaxError: multiple statements found while compiling a single statement
from datetime import datetime
import time
print ("time.ctime() : ",time.ctime())
time.ctime() :  Tue Dec  6 08:10:24 2022
dir(datetime)
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
dir(date)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dir(date)
NameError: name 'date' is not defined
print ("current : ",time.ctime())
current :  Tue Dec  6 08:12:01 2022
print ("time is:",time.time(),time.date())
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print ("time is:",time.time(),time.date())
AttributeError: module 'time' has no attribute 'date'
print ("time is:",time.time())
time is: 1670293742.1938674
print ("time is:",time.today())
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print ("time is:",time.today())
AttributeError: module 'time' has no attribute 'today'
print ("time is:",datetimetime.today())
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print ("time is:",datetimetime.today())
NameError: name 'datetimetime' is not defined
print ("time is:",datetime.today())
time is: 2022-12-06 08:15:12.334956
import sys
dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_deactivate_opcache', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
print(sys.version())
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(sys.version())
TypeError: 'str' object is not callable
print(sys.version)
3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)]
sys.platform
'win32'
sys.exit(1)
sys.modules
{'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module '_frozen_importlib' (frozen)>, '_imp': <module '_imp' (built-in)>, '_thread': <module '_thread' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_weakref': <module '_weakref' (built-in)>, '_io': <module '_io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'nt': <module 'nt' (built-in)>, 'winreg': <module 'winreg' (built-in)>, '_frozen_importlib_external': <module '_frozen_importlib_external' (frozen)>, 'time': <module 'time' (built-in)>, 'zipimport': <module 'zipimport' (frozen)>, '_codecs': <module '_codecs' (built-in)>, 'codecs': <module 'codecs' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\codecs.py'>, 'encodings.aliases': <module 'encodings.aliases' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\encodings\\aliases.py'>, 'encodings': <module 'encodings' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\encodings\\__init__.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\encodings\\utf_8.py'>, 'encodings.cp1252': <module 'encodings.cp1252' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\encodings\\cp1252.py'>, '_signal': <module '_signal' (built-in)>, '_abc': <module '_abc' (built-in)>, 'abc': <module 'abc' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\abc.py'>, 'io': <module 'io' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\io.py'>, '__main__': <module '__main__' (built-in)>, '_stat': <module '_stat' (built-in)>, 'stat': <module 'stat' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\stat.py'>, '_collections_abc': <module '_collections_abc' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\_collections_abc.py'>, 'genericpath': <module 'genericpath' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\genericpath.py'>, '_winapi': <module '_winapi' (built-in)>, 'ntpath': <module 'ntpath' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\ntpath.py'>, 'os.path': <module 'ntpath' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\ntpath.py'>, 'os': <module 'os' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\os.py'>, '_sitebuiltins': <module '_sitebuiltins' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\_sitebuiltins.py'>, '_distutils_hack': <module '_distutils_hack' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\_distutils_hack\\__init__.py'>, 'types': <module 'types' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\types.py'>, 'importlib._bootstrap': <module '_frozen_importlib' (frozen)>, 'importlib._bootstrap_external': <module '_frozen_importlib_external' (frozen)>, 'warnings': <module 'warnings' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\warnings.py'>, 'importlib': <module 'importlib' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\importlib\\__init__.py'>, 'importlib._abc': <module 'importlib._abc' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\importlib\\_abc.py'>, 'itertools': <module 'itertools' (built-in)>, 'keyword': <module 'keyword' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\keyword.py'>, '_operator': <module '_operator' (built-in)>, 'operator': <module 'operator' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\operator.py'>, 'reprlib': <module 'reprlib' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\reprlib.py'>, '_collections': <module '_collections' (built-in)>, 'collections': <module 'collections' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\collections\\__init__.py'>, '_functools': <module '_functools' (built-in)>, 'functools': <module 'functools' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\functools.py'>, 'contextlib': <module 'contextlib' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\contextlib.py'>, 'importlib.util': <module 'importlib.util' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\importlib\\util.py'>, 'importlib.machinery': <module 'importlib.machinery' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\importlib\\machinery.py'>, 'mpl_toolkits': <module 'mpl_toolkits' (<_frozen_importlib_external._NamespaceLoader object at 0x000001A1F71A1900>)>, 'pywin32_system32': <module 'pywin32_system32' (<_frozen_importlib_external._NamespaceLoader object at 0x000001A1F7169ED0>)>, 'pywin32_bootstrap': <module 'pywin32_bootstrap' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\win32\\lib\\pywin32_bootstrap.py'>, 'site': <module 'site' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site.py'>, 'idlelib': <module 'idlelib' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\__init__.py'>, 'enum': <module 'enum' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\enum.py'>, '_sre': <module '_sre' (built-in)>, 'sre_constants': <module 'sre_constants' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\sre_constants.py'>, 'sre_parse': <module 'sre_parse' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\sre_parse.py'>, 'sre_compile': <module 'sre_compile' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\sre_compile.py'>, '_locale': <module '_locale' (built-in)>, 'copyreg': <module 'copyreg' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\copyreg.py'>, 're': <module 're' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\re.py'>, 'token': <module 'token' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\token.py'>, 'tokenize': <module 'tokenize' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\tokenize.py'>, 'linecache': <module 'linecache' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\linecache.py'>, '_weakrefset': <module '_weakrefset' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\_weakrefset.py'>, 'threading': <module 'threading' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\threading.py'>, '_heapq': <module '_heapq' (built-in)>, 'heapq': <module 'heapq' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\heapq.py'>, '_queue': <module '_queue' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\_queue.pyd'>, 'queue': <module 'queue' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\queue.py'>, 'textwrap': <module 'textwrap' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\textwrap.py'>, 'traceback': <module 'traceback' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\traceback.py'>, '_string': <module '_string' (built-in)>, 'string': <module 'string' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\string.py'>, 'errno': <module 'errno' (built-in)>, 'signal': <module 'signal' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\signal.py'>, 'msvcrt': <module 'msvcrt' (built-in)>, 'subprocess': <module 'subprocess' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\subprocess.py'>, 'platform': <module 'platform' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\platform.py'>, '_tkinter': <module '_tkinter' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\_tkinter.pyd'>, 'tkinter.constants': <module 'tkinter.constants' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\tkinter\\constants.py'>, 'tkinter': <module 'tkinter' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\tkinter\\__init__.py'>, 'idlelib.multicall': <module 'idlelib.multicall' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\multicall.py'>, 'idlelib.autocomplete_w': <module 'idlelib.autocomplete_w' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\autocomplete_w.py'>, 'collections.abc': <module 'collections.abc' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\collections\\abc.py'>, 'configparser': <module 'configparser' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\configparser.py'>, 'idlelib.config': <module 'idlelib.config' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\config.py'>, 'idlelib.pyparse': <module 'idlelib.pyparse' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\pyparse.py'>, 'idlelib.hyperparser': <module 'idlelib.hyperparser' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\hyperparser.py'>, 'idlelib.autocomplete': <module 'idlelib.autocomplete' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\autocomplete.py'>, '_ast': <module '_ast' (built-in)>, 'ast': <module 'ast' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\ast.py'>, '_opcode': <module '_opcode' (built-in)>, 'opcode': <module 'opcode' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\opcode.py'>, 'dis': <module 'dis' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\dis.py'>, 'inspect': <module 'inspect' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\inspect.py'>, 'idlelib.tooltip': <module 'idlelib.tooltip' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\tooltip.py'>, 'idlelib.calltip_w': <module 'idlelib.calltip_w' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\calltip_w.py'>, 'idlelib.calltip': <module 'idlelib.calltip' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\calltip.py'>, 'posixpath': <module 'posixpath' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\posixpath.py'>, 'fnmatch': <module 'fnmatch' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\fnmatch.py'>, 'bdb': <module 'bdb' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\bdb.py'>, 'binascii': <module 'binascii' (built-in)>, 'math': <module 'math' (built-in)>, '_datetime': <module '_datetime' (built-in)>, 'datetime': <module 'datetime' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\datetime.py'>, '_struct': <module '_struct' (built-in)>, 'struct': <module 'struct' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\struct.py'>, 'xml': <module 'xml' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\xml\\__init__.py'>, 'xml.parsers': <module 'xml.parsers' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\xml\\parsers\\__init__.py'>, 'pyexpat.errors': <module 'pyexpat.errors'>, 'pyexpat.model': <module 'pyexpat.model'>, 'pyexpat': <module 'pyexpat' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\pyexpat.pyd'>, 'xml.parsers.expat.model': <module 'pyexpat.model'>, 'xml.parsers.expat.errors': <module 'pyexpat.errors'>, 'xml.parsers.expat': <module 'xml.parsers.expat' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\xml\\parsers\\expat.py'>, 'plistlib': <module 'plistlib' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\plistlib.py'>, 'test': <module 'test' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\test\\__init__.py'>, 'sysconfig': <module 'sysconfig' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\sysconfig.py'>, 'unittest.util': <module 'unittest.util' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\unittest\\util.py'>, 'unittest.result': <module 'unittest.result' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\unittest\\result.py'>, 'difflib': <module 'difflib' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\difflib.py'>, 'weakref': <module 'weakref' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\weakref.py'>, 'copy': <module 'copy' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\copy.py'>, 'dataclasses': <module 'dataclasses' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\dataclasses.py'>, 'pprint': <module 'pprint' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\pprint.py'>, 'unittest.case': <module 'unittest.case' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\unittest\\case.py'>, 'unittest.suite': <module 'unittest.suite' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\unittest\\suite.py'>, 'unittest.loader': <module 'unittest.loader' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\unittest\\loader.py'>, 'gettext': <module 'gettext' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\gettext.py'>, 'argparse': <module 'argparse' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\argparse.py'>, 'unittest.signals': <module 'unittest.signals' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\unittest\\signals.py'>, 'unittest.runner': <module 'unittest.runner' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\unittest\\runner.py'>, 'unittest.main': <module 'unittest.main' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\unittest\\main.py'>, 'unittest': <module 'unittest' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\unittest\\__init__.py'>, 'test.support.testresult': <module 'test.support.testresult' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\test\\support\\testresult.py'>, '_testcapi': <module '_testcapi' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\_testcapi.pyd'>, 'test.support': <module 'test.support' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\test\\support\\__init__.py'>, 'idlelib.macosx': <module 'idlelib.macosx' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\macosx.py'>, 'idlelib.scrolledlist': <module 'idlelib.scrolledlist' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\scrolledlist.py'>, 'idlelib.window': <module 'idlelib.window' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\window.py'>, 'idlelib.debugger': <module 'idlelib.debugger' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\debugger.py'>, 'idlelib.debugger_r': <module 'idlelib.debugger_r' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\debugger_r.py'>, '_compat_pickle': <module '_compat_pickle' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\_compat_pickle.py'>, '_pickle': <module '_pickle' (built-in)>, 'pickle': <module 'pickle' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\pickle.py'>, 'select': <module 'select' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\select.pyd'>, '_socket': <module '_socket' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\_socket.pyd'>, 'selectors': <module 'selectors' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\selectors.py'>, 'socket': <module 'socket' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\socket.py'>, 'socketserver': <module 'socketserver' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\socketserver.py'>, 'idlelib.rpc': <module 'idlelib.rpc' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\rpc.py'>, 'idlelib.debugobj_r': <module 'idlelib.debugobj_r' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\debugobj_r.py'>, 'shlex': <module 'shlex' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\shlex.py'>, 'zlib': <module 'zlib' (built-in)>, '_compression': <module '_compression' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\_compression.py'>, '_bz2': <module '_bz2' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\_bz2.pyd'>, 'bz2': <module 'bz2' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\bz2.py'>, '_lzma': <module '_lzma' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\DLLs\\_lzma.pyd'>, 'lzma': <module 'lzma' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\lzma.py'>, 'shutil': <module 'shutil' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\shutil.py'>, '_bisect': <module '_bisect' (built-in)>, 'bisect': <module 'bisect' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\bisect.py'>, '_random': <module '_random' (built-in)>, '_sha512': <module '_sha512' (built-in)>, 'random': <module 'random' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\random.py'>, 'tempfile': <module 'tempfile' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\tempfile.py'>, 'idlelib.util': <module 'idlelib.util' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\util.py'>, 'idlelib.iomenu': <module 'idlelib.iomenu' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\iomenu.py'>, 'idlelib.zoomheight': <module 'idlelib.zoomheight' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\zoomheight.py'>, 'idlelib.tree': <module 'idlelib.tree' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\tree.py'>, 'idlelib.debugobj': <module 'idlelib.debugobj' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\debugobj.py'>, 'idlelib.stackviewer': <module 'idlelib.stackviewer' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\stackviewer.py'>, 'idlelib.run': <module 'idlelib.run' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\idlelib\\run.py'>, 'pkgutil': <module 'pkgutil' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\pkgutil.py'>, 'urllib': <module 'urllib' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\urllib\\__init__.py'>, 'urllib.parse': <module 'urllib.parse' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\urllib\\parse.py'>, 'pydoc': <module 'pydoc' from 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python310\\lib\\pydoc.py'>}
import re
regex = r"([a-z]+t)"

test_str = "the cat sat on the mat"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

SyntaxError: multiple statements found while compiling a single statement

======================== RESTART: C:/spython92/12.py ========================
Traceback (most recent call last):
  File "C:/spython92/12.py", line 5, in <module>
    matches = re.finditer(regex, test_str, re.MULTILINE)
NameError: name 're' is not defined

======================== RESTART: C:/spython92/12.py ========================
Match 1 was found at 4-7: cat
Group 1 found at 4-7: cat
Match 2 was found at 8-11: sat
Group 1 found at 8-11: sat
Match 3 was found at 19-22: mat
Group 1 found at 19-22: mat

======================== RESTART: C:/spython92/12.py ========================
Match 1 was found at 4-7: cat
Group 1 found at 4-7: cat
Match 2 was found at 8-11: sat
Group 1 found at 8-11: sat
Match 3 was found at 19-22: mat
Group 1 found at 19-22: mat
Match 1 was found at 11-15:  on 
Group 1 found at 12-14: on

======================== RESTART: C:/spython92/12.py ========================
Match 1 was found at 11-15:  on 
Group 1 found at 12-14: on

======================== RESTART: C:/spython92/12.py ========================
Match 1 was found at 0-4: 2022
Group 1 found at 0-4: 2022

======================== RESTART: C:/spython92/12.py ========================
Match 1 was found at 45-57: programming.
Group 1 found at 45-56: programming
square=[]
for num in range(10)
SyntaxError: incomplete input
for num in range(10):
    square.append(num**2)

    
print ("squares:",square)
squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
SyntaxError: incomplete inputfor num in range(10):
    square.append(num**2)
    
SyntaxError: invalid syntax

[x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[x**2 for x in range(10)]:
    
SyntaxError: incomplete input
[x**2 if x % 2 == 0 else x**3 for x in range(10)]
[0, 1, 4, 27, 16, 125, 36, 343, 64, 729]
[0, 1, 4, 27, 16, 125, 36, 343, 64, 729]
[0, 1, 4, 27, 16, 125, 36, 343, 64, 729]
[x for x in range(10) if x % 2 == 0]
[0, 2, 4, 6, 8]
[x for x in range(10) if x % 2 == 0][x**2 if x % 2 == 0 else x**3 for x in range(10)]
SyntaxError: invalid syntax
[x**2 if x % 2 == 0 for x in range(10)]
SyntaxError: expected 'else' after 'if' expression
[x**2 for x in range(10) if x%==0]
SyntaxError: invalid syntax
[x**2 for x in range(10) if x%2==0]
[0, 4, 16, 36, 64]
[0, 4, 16, 36, 64]
[0, 4, 16, 36, 64]
l=list(range(1,100,4))
for key,value in enumerate(l):
    print(key,"::",value)

    
0 :: 1
1 :: 5
2 :: 9
3 :: 13
4 :: 17
5 :: 21
6 :: 25
7 :: 29
8 :: 33
9 :: 37
10 :: 41
11 :: 45
12 :: 49
13 :: 53
14 :: 57
15 :: 61
16 :: 65
17 :: 69
18 :: 73
19 :: 77
20 :: 81
21 :: 85
22 :: 89
23 :: 93
24 :: 97
l=list(range(1,100))
for key,value in enumerate(l):
    print(key,"::",value)

    
0 :: 1
1 :: 2
2 :: 3
3 :: 4
4 :: 5
5 :: 6
6 :: 7
7 :: 8
8 :: 9
9 :: 10
10 :: 11
11 :: 12
12 :: 13
13 :: 14
14 :: 15
15 :: 16
16 :: 17
17 :: 18
18 :: 19
19 :: 20
20 :: 21
21 :: 22
22 :: 23
23 :: 24
24 :: 25
25 :: 26
26 :: 27
27 :: 28
28 :: 29
29 :: 30
30 :: 31
31 :: 32
32 :: 33
33 :: 34
34 :: 35
35 :: 36
36 :: 37
37 :: 38
38 :: 39
39 :: 40
40 :: 41
41 :: 42
42 :: 43
43 :: 44
44 :: 45
45 :: 46
46 :: 47
47 :: 48
48 :: 49
49 :: 50
50 :: 51
51 :: 52
52 :: 53
53 :: 54
54 :: 55
55 :: 56
56 :: 57
57 :: 58
58 :: 59
59 :: 60
60 :: 61
61 :: 62
62 :: 63
63 :: 64
64 :: 65
65 :: 66
66 :: 67
67 :: 68
68 :: 69
69 :: 70
70 :: 71
71 :: 72
72 :: 73
73 :: 74
74 :: 75
75 :: 76
76 :: 77
77 :: 78
78 :: 79
79 :: 80
80 :: 81
81 :: 82
82 :: 83
83 :: 84
84 :: 85
85 :: 86
86 :: 87
87 :: 88
88 :: 89
89 :: 90
90 :: 91
91 :: 92
92 :: 93
93 :: 94
94 :: 95
95 :: 96
96 :: 97
97 :: 98
98 :: 99
>>> i = (str(i) for i in range(10))
>>> print(list(i))
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> print([str(i) for i in range(10)])
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> print([(i) for i in range(10)])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
