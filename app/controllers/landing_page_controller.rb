class LandingPageController < ApplicationController
  def home
  	@user = User.create!
  	# @user = User.first
  	@before_preferences = BeforePreference.create!(:name => "Song-1",:user_id => @user.id)
  	@after_preferences = AfterPreference.create!(:name => "Song-1",:user_id => @user.id)
  	@before_preferences = BeforePreference.create!(:name => "Song-3",:user_id => @user.id)
  	@after_preferences = AfterPreference.create!(:name => "Song-3",:user_id => @user.id)
  	@before_preferences = BeforePreference.create!(:name => "Song-2",:user_id => @user.id)
  	@after_preferences = AfterPreference.create!(:name => "Song-2",:user_id => @user.id)
  	@user.save!

  	# redirect_to landing_page_path
  end
end
