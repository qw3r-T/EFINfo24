# frozen_string_literal: true

def contains_threes(list)
  return_list = []
  list.each do |element|
    return_list << element if (element % 3).zero?
  end
  return_list.sort
end

puts contains_threes([1,3,4,6,7,12,9])
