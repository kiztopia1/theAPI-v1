
const log = value => console.log(value)
    const POS = {
        delimiters: ['[[', ']]'],
        data () {
            return{
                productsOnFilter: [],
                activeProduct: [],
                productsOnCart: [],
                productInput: '',
                product : null,
                product_amount: 1,
                product_total: 0,
                product_price: 0,
                product_id: undefined,

                cart_total: 0,
                cart_tax: 0,
                cart_aft_total:0,

                errors: [],
                products: '',
                total: 0,
                id: '',
            }
        },
        // this will allow as to add pre calculated values
        // and we can call them from the template by using '{{ computed function name}}'
        computed: {
            
        },
        mounted() {
            this.sale_product_handler()
            // check if we are in sale and focus the input
            if ( document.getElementById('item')){

                document.getElementById('item').focus()
            }
            let pos = document.getElementById('pos')
            document.addEventListener("keydown", (event) => {
                log(event.code)
                // handle keypress
                if (event.code == 'F1'){
                    event.preventDefault()
                    if(document.getElementById('sale_form')){

                        document.getElementById('close_pos').click()
                    }else{
                        document.getElementById('to_sale_nav').click()
                    }
                }else if (event.code == 'Enter'){
                    


                    this.product_Form_handler()
                    
                }else if (event.code == 'NumpadAdd'){
                    
                    this.add_to_cart()
                }
                else if (event.code == 'NumpadEnter'){
                    
                    document.getElementById('sale_form').click()
                }else if (event.code == 'ControlLeft' || event.code == 'ControlRight'){
                    if(document.getElementById('close_pos')){

                        document.getElementById('close_pos').click()
                    }else if(document.getElementById('to_sale_nav')){
                        document.getElementById('to_sale_nav').click()
                    }
                }
            });
        },
            // 27 esk , f1  
        methods :{
            sale_product_handler () {
                let data = []
                let products = document.querySelectorAll('.sale_products_text')
                Array.from(products).forEach(function(product, index){
                    let value = product.innerHTML
                    
                    let p = ''
                    let new_product = JSON.parse(value)
                    new_product.forEach(product => {
                        p += `<p class='dark'>
                        ${product.amount}  :  ${product.description} 
                        </p>`
                    })
                    product.innerHTML = p
                    data.push(new_product)
                    
                })
            },
            async get_product (value)   {
                let param = `http://localhost:8000/api/v1/products/${value}`
                let response = await fetch(param)
                let product = await response.json();
                return product
            },
            async product_Form_handler () {
                const new_product = await this.get_product(this.productInput)
                this.productInput = ''
                document.getElementById('qty').focus()
                if(new_product.price){
                    this.product = new_product
                    this.product_price = this.product.price
                    this.product_total = this.product.price * this.product_amount
                    this.product_id = this.product.id
                    this.errors = []
                }else{
                    this.errors.push({
                        'type': 'error',
                        'value': "incorrect product code"
                    })
                }
            },
            add_to_cart () {
                if (this.product){
                    const product = {
                        'id': this.product.id,
                        'description': this.product.description,
                        'price': this.product.price,
                        'amount': this.product_amount,
                        'tax': this.product.tax 
                    }
                    this.productsOnCart.push(product)
                    this.cart_total_calc()
                    this.update_form()
                    this.errors = []
                    this.productInput = ''
                }else{
                    this.errors.push({
                        'type': 'error',
                        'value': "no product selected"
                    })
                    
                }
                
            },
            product_total_calc () {
                
                if (this.product_amount == ''){
                    this.errors.push({
                        'type': 'error',
                        'value': "incorrect amount"
                    })
                    this.product_amount = 1
                }else{
                    let product_total = this.product.price * this.product_amount 
                    this.product_total = product_total
                    this.errors = []
                }
            },
            // calculate the total cart value from cart products
            cart_total_calc () {
                let cart_total = 0
                 
                this.productsOnCart.forEach(element => {
                    cart_total += element.price * element.amount
                });
                this.cart_total = cart_total
                this.cart_tax = Math.round(cart_total * 0.15)
                this.cart_aft_total = cart_total + this.cart_tax
                document.getElementById('item').value = ''
                
                
            },
            // delete cart item function
            del_cart_product (selected_index) {
                let selected_product = {}
                this.productsOnCart.forEach((product,index) => {
                    
                    if(index == selected_index){
                        selected_product = product
                    }
                })

                const data = this.productsOnCart.filter(function(product){
                    
                    return product != selected_product
                })
                
                this.productsOnCart = data
                this.products = JSON.stringify(this.productsOnCart)
                this.cart_total_calc()
                this.total = this.cart_total

            },
            update_form() {
                this.products = JSON.stringify(this.productsOnCart)
                this.total = this.cart_total
                this.id = Date.now()
                document.getElementById('item').focus()
                setTimeout(()=>{
                    this.productInput = ''
                },10)
                
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
