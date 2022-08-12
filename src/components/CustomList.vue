<template>
  <q-expansion-item v-if="item.type == 'directory'" dense :label="item.name" expand-separator :header-inset-level="inset" :content-inset-level="inset + insetStep">
    <custom-list
          v-for="child in item.children"
          :key="child"
          :item="child"
          :inset="inset"

        />
  </q-expansion-item>
  <q-item v-else clickable @click="openNote(item)" dense  >
    <q-item-section>
      <q-item-label>{{ item.name }}</q-item-label>
    </q-item-section>

  </q-item>
</template>

<script>
import router from 'src/router'
import { useRouter } from 'vue-router'

export default {
  name: 'CustomList',
  props: {
    item: {
      type: Object,
      required: true
    },
    inset: {
      type: Number,
      default: 0
    },
    insetStep: {
      type: Number,
      default: 0.25
    }
  },
  setup () {
    const router = useRouter()

    const openNote = (note) => {
      console.log(note)
      router.push(note.src.replace('..', ''))
    }
    return {
      openNote
    }
  }
}
</script>
