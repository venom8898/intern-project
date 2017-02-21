class Dessert
    attr_accessor :name
    attr_accessor :calories
     
  def initialize(name, calories)
    @name=name
    @calories = calories
    
   if @calories <0
    raise ArgumentError
   end
    
  end
  def healthy?
   if @calories < 200
   return true
   else
   return false
   end 
  end
  
  def delicious?
    return true unless @flavor == "licorice"
  end

end

class JellyBean < Dessert
  def initialize(flavor)
    @flavor=flavor
    @name = @flavor + " jelly bean"
    @calories=5
  end
  # your code here
end
