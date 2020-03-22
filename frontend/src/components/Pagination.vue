<template>
  <ul class="pagination">
    <li class="pagination-item">
      <button type="button"
              @click="onClickFirstPage"
              :disabled="isFirstPage"
              >
        First
      </button>
    </li>
    <li class="pagination-item">
      <button type="button"
              @click="onClickPreviousPage"
              :disabled="isFirstPage"
              >
        Previous
      </button>
    </li>
    <li v-for="page in pages"
        :key="page.index"
        class="pagination-item">
      <button type="button"
              @click="onClickPage(page.index)"
              :disabled="page.isDisabled"
              :class="{active: isPageActive(page.index)}"
              >
        {{page.index}}
      </button>
    </li>
    <li class="pagination-item">
      <button type="button"
              @click="onClickNextPage"
              :disabled="isLastPage"
              >
        Next
      </button>
    </li>
    <li class="pagination-item">
      <button type="button"
              @click="onClickLastPage"
              :disabled="isLastPage"
              >
        Last
      </button>
    </li>
  </ul>
</template>
<script>
  export default {
    props: {
      maxVisibleButtons: {
        type: Number,
        required: false,
        default: 5
      },
      totalPages: {
        type: Number,
        required: true
      },
      currentPage: {
        type: Number,
        required: true
      }
    },
    computed: {
      startPage() {
        if (this.currentPage === 1) {
          return 1
        } else if (this.currentPage === this.totalPages) {
          return Math.max(this.totalPages - this.maxVisibleButtons + 1, 1)
        } else {
          return Math.max(this.currentPage - Math.floor(this.maxVisibleButtons / 2), 1)
        }
      },
      endPage() {
        return Math.min(this.startPage + this.maxVisibleButtons - 1, this.totalPages)
      },
      pages() {
        const range = []

        for (let i = this.startPage; i <= this.endPage; i += 1) {
          range.push({ index: i, isDisabled: i === this.currentPage })
        }

        return range
      },
      isFirstPage() {
        return this.currentPage === 1
      },
      isLastPage() {
        return this.currentPage === this.totalPages
      }
    },
    methods: {
      onClickFirstPage() {
        this.$emit('pagechanged', 1)
      },
      onClickPreviousPage() {
        this.$emit('pagechanged', this.currentPage - 1)
      },
      onClickPage(page) {
        this.$emit('pagechanged', page)
      },
      onClickNextPage() {
        this.$emit('pagechanged', this.currentPage + 1)
      },
      onClickLastPage() {
        this.$emit('pagechanged', this.totalPages)
      },
      isPageActive(page) {
        return this.currentPage === page
      }
    }
  }
</script>
