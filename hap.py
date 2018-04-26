def union(a, b, testing = True):
  if testing: print "Testing union on " + str(a) + ' & ' + str(b) + '...'
  return a + [i for i in b if i not in a]

def intersection(a, b, testing = True ):
  if testing: print "Testing intersect on " + str(a) + ' & ' + str(b) + '...'
  return [x for x in a if x in b]

def set_diff(a, b, testing = True):
  if testing: print "Testing set difference on " + str(a) + ' & ' + str(b) + '...'
  return [i for i in a if i not in intersection(a, b, testing = False) ]

def sym_diff(a, b, testing = True):
  if testing: print "Testing symmetric difference on " + str(a) + ' & ' + str(b) + '...'
  return set_diff(a, b, testing = False) + set_diff(b, a, testing = False)

def cart_prod(a, b, testing = True):
  if testing: print "Testing cartesian product on " + str(a) + ' & ' + str(b) + '...'
  return [(i,j) for i in a for j in b]


print intersection([1, 2], [3, 4])
print intersection([1, 2, 3], [3, 4])
print intersection([1, 2, 3], [1, 2])

print union([1, 2], [3, 4])
print union([1, 2, 3], [3, 4])
print union([1, 2, 3], [1, 2])

print set_diff([1, 2], [3, 4])
print set_diff([1, 2, 3], [3, 4])
print set_diff([1, 2, 3], [1, 2])

print sym_diff([1, 2], [3, 4])
print sym_diff([1, 2, 3], [3, 4])
print sym_diff([1, 2, 3], [1, 2])

print cart_prod([1, 2], [3, 4])
print cart_prod([1, 2, 3], [3, 4])
print cart_prod([1, 2, 3], [1, 2])
print cart_prod([1, 2], ['red', 'white'])

# uniqA = [x for x in a if x not in b]
# uniqB = [y for y in b if y not in a]
