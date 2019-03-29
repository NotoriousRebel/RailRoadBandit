class ChybetaController < ApplicationController
    def index
        render file: "#{Rails.root}/app/views/chybeta/index.html.erb"
    end
end
