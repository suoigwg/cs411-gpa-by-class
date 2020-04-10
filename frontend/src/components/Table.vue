<template>
  <div>
    <md-table>
      <md-table-row class="float-center">
        <!-- eslint-disable-next-line vue/no-unused-vars -->
        <md-table-head v-for="(value, key) in items[0]" :key="key" v-if="key !== 'id'">{{key}}</md-table-head>
      </md-table-row>
      <!-- eslint-disable-next-line vue/valid-v-for -->
      <md-table-row v-for="(item, index) in currentItems" :key="index">
        <md-table-cell v-for="(value, key) in item" :key="key" v-if="key !== 'id'">{{value}}</md-table-cell>
      </md-table-row>
    </md-table>
    <Pagination class="d-flex justify-content-center" :total-pages="totalPages" :current-page="currentPage" @pagechanged="onPageChange"></Pagination>
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
      },
      currentPage: {
        type: Number,
        required: false,
        default: 1
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
    }
  }
</script>

<style scoped>
  .md-table-head {
    text-align: center;
  }
</style>
