export const state = () => ({
  userType: null
})

export const mutations = {
  changeUserType(state, mode) {
    state.userType = mode
  }
}
