export default {
  state: {
    username: 'Chen',
    isAdmin: true,
    loggedIn: true,
    newItems: [],
    updatedItems: [],
    deletedItems: []
  },

  clearEdit() {
    this.state.newItems = []
    this.state.updatedItems = []
    this.state.deletedItems = []
  }
}
