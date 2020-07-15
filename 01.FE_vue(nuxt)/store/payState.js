export const state = () => ({
  payment: false
})

export const mutations = {
  changePayment(state) {
    state.payment = !state.payment
  }
}
