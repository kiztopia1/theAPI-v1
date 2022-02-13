let nav = $('.mobile_nav'),
    dashboard = $('.dashboard')

console.log(nav)

nav.click(function () {
    console.log('yes')
    dashboard.toggleClass('mobile_nav__active')
})
