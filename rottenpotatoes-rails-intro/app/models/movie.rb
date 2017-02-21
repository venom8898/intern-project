class Movie < ActiveRecord::Base

 def self.all_ratings
  movieList = Array.new
  self.select("rating").uniq.each {|x| movieList.push(x.rating)}
  movieList.sort.uniq
 end   
end
