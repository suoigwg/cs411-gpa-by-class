<template>
  <div>
    <md-table>
      <md-table-row class="float-center">
        <!-- eslint-disable-next-line vue/no-unused-vars -->
        <md-table-head v-for="(value, key) in items[0]" :key="key" v-if="key !== 'id'">{{key}}</md-table-head>
        <md-table-head></md-table-head>
      </md-table-row>
      <!--Display current items-->
      <!-- eslint-disable-next-line vue/valid-v-for -->
      <md-table-row v-for="(item, index) in currentItems" :key="index">
        <md-table-cell v-for="(value, key) in item" :key="key" v-if="key !== 'id'">
          <textarea v-model="item[key]"
                    @input="updateItem(index)">
          </textarea>
        </md-table-cell>
        <md-table-cell>
          <button class="btn btn-danger"
                  @click="deleteItem(item)">
            Delete
          </button>
        </md-table-cell>
      </md-table-row>
      <!--Display newly added items-->
      <!-- eslint-disable-next-line vue/valid-v-for -->
      <md-table-row v-for="(item, index) in store.state.newItems" :key="index + currentItems.length">
        <md-table-cell v-for="(value, key) in item" :key="key" v-if="key !== 'id'">
          <textarea v-model="item[key]"></textarea>
        </md-table-cell>
        <md-table-cell>
          <button class="btn btn-danger"
                  @click="deleteNewItem(item)">
            Delete
          </button>
        </md-table-cell>
      </md-table-row>
      <!--Display add new item row-->
      <md-table-row>
        <md-table-cell v-for="(value, key) in newItem" :key="key" v-if="key !== 'id'">
          <textarea v-model="newItem[key]"></textarea>
        </md-table-cell>
        <md-table-cell>
          <button class="btn btn-primary"
                  @click="addItem">
            Add New
          </button>
        </md-table-cell>
      </md-table-row>
    </md-table>
    <Pagination class="d-flex justify-content-center" :total-pages="totalPages" :current-page="currentPage" @pagechanged="onPageChange"></Pagination>
  </div>
</template>

<script>
  import Pagination from '@/components/Pagination'
  import store from '@/store.js'

  export default {
    components: { Pagination },

    props: {
      items: {
        type: Array,
        required: true
      },
      itemsPerPage: {
        type: Number,
        required: false,
        default: 5
      },
      currentPage: {
        type: Number,
        required: false,
        default: 1
      }
    },

    data() {
      return {
        store: store,
        newItem: Object.assign({}, this.items[0])
      }
    },

    computed: {
      totalPages() {
        return Math.ceil(this.items.length / this.itemsPerPage)
      },
      firstItemIndex() {
        return (this.currentPage - 1) * this.itemsPerPage
      },
      lastItemIndex() {
        return Math.min(this.firstItemIndex + this.itemsPerPage, this.items.length)
      },
      currentItems() {
        return this.items.slice(this.firstItemIndex, this.lastItemIndex)
      }
    },

    methods: {
      onPageChange(page) {
        this.$emit('pagechanged', page)
      },

      deleteItem(item) {
        let index = this.items.indexOf(item)
        if (index !== -1) {
          this.items.splice(index, 1)
          store.state.deletedItems.push(item)
        }
      },

      deleteNewItem(item) {
        let index = store.state.newItems.indexOf(item)
        if (index !== -1) {
          store.state.newItems.splice(index, 1)
        }
      },

      updateItem(itemId) {
        let index = itemId + this.itemsPerPage * (this.currentPage - 1)
        if (!store.state.updatedItems.includes(index)) {
          console.log(index)
          store.state.updatedItems.push(index)
        }
      },

      addItem() {
        store.state.newItems.push(Object.assign({}, this.newItem))
        this.clearNewItem()
      },

      clearNewItem() {
        for (const property in this.newItem) {
          this.newItem[property] = ''
        }
      }
    },

    created() {
      this.clearNewItem()
    }
  }
</script>

<style scoped>
  td textarea {
    width: 100%;
    resize: none;
}
</style>
