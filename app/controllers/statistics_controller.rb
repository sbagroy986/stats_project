class StatisticsController < ApplicationController
  def view
  	@user = User.all
  	@users_count = @user.count
  	@users_song1
  end
end
