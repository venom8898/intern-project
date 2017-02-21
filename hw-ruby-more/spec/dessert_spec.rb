require 'dessert'
require 'byebug'
require 'rspec/its'

describe Dessert do
  describe 'cake' do
    subject { Dessert.new('cake', 400) }
    its(:calories) { should == 400 }
    its(:name)     { should == 'cake' }
    it { should be_delicious }
    it { should_not be_healthy }
  end

 describe 'apple' do
    subject { Dessert.new('apple', 75) }
    it { should be_delicious }
    it { should be_healthy }
  end
  describe 'can set' do
    before(:each) { @dessert = Dessert.new('xxx', 0) }
    it 'calories' do
      @dessert.calories = 80
      expect(@dessert.calories).to eq(80)
    end
    it 'name' do
      @dessert.name = 'ice cream'
      expect(@dessert.name).to eq('ice cream')
    end
=begin   
    
  describe 'lettuce' do
    subject { Dessert.new('lettuce', -10) }
    it { should raise_error(ArgumentError) }
  end
    describe 'starbucks' do
    subject { Dessert.new('starbucks', 'they dont want you to know') }
    it { should raise_error(ArgumentError) }
  end
  
=end  
  end
end

describe JellyBean do
  describe 'when non-licorice' do
    subject { JellyBean.new('vanilla') }
    its(:calories) { should == 5 }
    its(:name)     { should match /vanilla jelly bean/i }
    it             { should be_delicious }
  end
  describe 'when licorice' do
    subject { JellyBean.new('licorice') }
    it { should_not be_delicious }
  end
end


  describe 'constructor' do
    it 'no negative calories' , points: 10 do
      expect {  Dessert.new('lettuce', -10) }.to raise_error(ArgumentError)
    end
    it 'no string for calories' , points: 10 do
      expect {  Dessert.new( 'starbucks', 'they dont want you to know') }.to raise_error(ArgumentError)
    end
end