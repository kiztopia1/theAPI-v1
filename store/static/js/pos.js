
    const POS = {
        delimiters: ['[[', ']]'],
        data () {
            return{
                deckName: 'POS',
                productsOnFilter: [],
                activeProduct: [],
                productsOnCart: [],
                productInput: '',
                product : null,
                product_amount: 1,
                product_total: 0,
                product_price: 0,
                cart_total: 0,
                errors: []
            }
        },
        // this will allow as to add pre calculated values
        // and we can call them from the template by using '{{ computed function name}}'
        computed: {
            
        },
        methods :{
            async get_product (value)   {
                let param = `http://localhost:8000/api/v1/products/${value}`
                let response = await fetch(param)
                let product = await response.json();
                return product
            },
            async product_Form_handler () {
                const new_product = await this.get_product(this.productInput)
                this.product = new_product
                this.product_price = this.product.price
                this.product_total = this.product.price * this.product_amount
            },
            add_to_cart () {
                if (this.product){
                    const product = {
                        'description': this.product.description,
                        'price': this.product.price,
                        'amount': this.product_amount,
                        'tax': this.product.tax 
                    }
                    this.productsOnCart.push(product)
                    this.cart_total_calc()
                    this.errors = []
                }else{
                    this.errors.push({
                        'type': 'error',
                        'value': "no product selected"
                    })
                    console.log(this.errors)
                }
            },
            product_total_calc () {
                let product_total = this.product.price * this.product_amount 
                this.product_total = product_total
            },
            // calculate the total cart value from cart products
            cart_total_calc () {
                let cart_total = 0
                this.productsOnCart.forEach(element => {
                    cart_total += element.price * element.amount
                });
                this.cart_total = cart_total
            },
            // delete cart item function
            del_cart_product (selected_index) {
                let selected_product = {}
                this.productsOnCart.forEach((product,index) => {
                    console.log(product)
                    if(index == selected_index){
                        selected_product = product
                    }
                })

                const data = this.productsOnCart.filter(function(product){
                    return product != selected_product
                })
                this.productsOnCart = data
            }
            


        },
        watch: {

            product_amount: function () {
                if(this.product){
                    this.product_total_calc()
                }
            },
        }
        
    };
    const app = Vue.createApp(POS);


    app.mount('#POS')
