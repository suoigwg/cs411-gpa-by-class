<template>
  <div>
    <table class="table table-bordered table-hover">
      <thead>
        <tr>
          <!-- eslint-disable-next-line vue/no-unused-vars -->
            <th v-for="[key, value] in Object.entries(items[0])" :key="key">{{key}}</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <!-- eslint-disable-next-line vue/require-v-for-key -->
          <tr v-for="item in currentItems">
            <td v-for="[key, value] in Object.entries(item)" :key="key">{{value}}</td>
            <td>
              <button>Edit</button>
            </td>
          </tr>
        </tbody>
      </table>
      <button>Add New</button>
      <Pagination :total-pages="totalPages" :current-page="currentPage" @pagechanged="onPageChange"></Pagination>
    </div>
  </template>

  <script>
    import Pagination from '@/components/Pagination'

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
        }
      },
      data() {
        return {
          currentPage: 1
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
          console.log(page)
          this.currentPage = page
        },
      }
    }
  </script>
