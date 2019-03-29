Rails.application.routes.draw do
# For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
    root 'application#hello'
    get 'chybeta/index' => 'chybeta#index'
    resources :chybeta
    root 'chybeta#index'
end
