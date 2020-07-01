export const state = () => ({
  payOn: false
})

export const mutations = {
  changePayment(state, payOn) {
    state.payOn = payOn
  }
}
