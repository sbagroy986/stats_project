class CreateBeforePreferences < ActiveRecord::Migration
  def change
    create_table :before_preferences do |t|
      t.string :name
      t.integer :order

      t.timestamps null: false
    end
  end
end
