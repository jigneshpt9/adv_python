import sys
def sort_words(input):
  words = input.split()
  words = [ w.lower() + w for w in words]
  print(words)
  words.sort()
  words = [w[len(w)/2:] for w in words]
  return ' '.join(words)

if __name__ == '__main__':
  print((sys.argv))
  out=sort_words(str(sys.argv[1]))
  print(out)
