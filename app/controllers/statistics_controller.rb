class StatisticsController < ApplicationController
  def view
  	@users = User.all
  	@users_count = @users.count
  end
end
