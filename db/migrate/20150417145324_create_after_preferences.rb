class CreateAfterPreferences < ActiveRecord::Migration
  def change
    create_table :after_preferences do |t|
      t.string :name
      t.integer :order

      t.timestamps null: false
    end
  end
end
