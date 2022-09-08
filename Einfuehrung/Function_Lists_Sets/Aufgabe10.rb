def is_anagram?(a,b)
  if a.split('').sort == b.split('').sort
    return true
  end
  return false
end

puts is_anagram? 'aabb','abab'
puts is_anagram? 'aabb','ababc'
