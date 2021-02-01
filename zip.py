import zipfile
f = zipfile.ZipFile('dist/h-breaker.zip', 'w', zipfile.ZIP_DEFLATED)
f.write('dist/h-breaker.exe', 'h-breaker.exe')
f.close()