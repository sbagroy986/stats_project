json.array!(@users) do |user|
  json.extract! user, :id, :after_song1, :after_song2, :after_song3, :before_song1, :before_song2, :before_song3, :completed
  json.url user_url(user, format: :json)
end
