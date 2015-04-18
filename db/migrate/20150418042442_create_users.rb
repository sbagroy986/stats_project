class CreateUsers < ActiveRecord::Migration
  def change
    create_table :users do |t|
      t.string :after_song1
      t.string :after_song2
      t.string :after_song3
      t.string :before_song1
      t.string :before_song2
      t.string :before_song3
      t.integer :completed

      t.timestamps null: false
    end
  end
end
