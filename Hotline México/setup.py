import cx_Freeze

executables = [cx_Freeze.Executable('linea caliente.py')]

cx_Freeze.setup(
    name = "pong 5 a bola esta esquentando",
    options = {'build_exe': {'packages':['pygame'],
                             'include_files':['imagens']}},
    executables = executables
)