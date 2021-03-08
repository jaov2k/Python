seconds = int(input("Enter the elapsed time in seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = ((seconds % 3600) % 60)
print (f'The elapsed time in seconds = {seconds}\n'
       f'The equivalent time in hours:minutes:seconds = {hours}:{minutes}:{secs}')