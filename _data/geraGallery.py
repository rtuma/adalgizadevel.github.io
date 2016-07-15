f = open('gallery.yml', 'w')

for i in range(1,178+1):
    f.write('  - image: quadro%03d.jpg\n'%i)
    f.write('    image-full: quadro%03d.jpg\n'%i)
    f.write('    index: %d\n'%i)
    f.write('    title:\n')
    f.write('    categories:\n')
    f.write('      - name: Abstrato\n')
    
