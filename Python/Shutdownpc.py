import os
if (shutdown := input("Do you want to shutdown your computer (yes / no): ")) == 'yes':
    os.system("shutdown /s /t 1")
else:
    print('Shutdown is not requested')                                               
