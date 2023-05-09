<script setup>
import { reactive, ref } from 'vue';
import axios from 'axios';
import store from './../store';
const initFormData = {
    title: '',
    slug: '',
    content: ''
}
const formData = reactive({ ...initFormData })
const error = ref({})
const onGenerateSlug = (event) => {
    // formData.slug = slugify(event.target.value);
}

const handleSubmitForm = async (event) => {
    const target = event.target
    const innerFormData = new FormData(target)
    const innerFormDataJson = JSON.stringify(Object.fromEntries(innerFormData))
    const formDataJson = JSON.stringify(formData)
    const csrfToken = store.token;
    const axiosConfig = {
        headers: {
            "X-CSRFToken": csrfToken,
        }
    }
    let response;
    try {
        response = await axios.post('/api/posts/create/', formDataJson, axiosConfig)
    } catch (e) {
        response = e.response
        error.value = e.response

        console.log(error.value)
    }
    if (response.status === 201) {
        for (let key of Object.keys(formData)) {
            formData[key] = initFormData[key]
        }
    }
    if (response.status === 500) {
        alert('Erreur serveur, merci de réitérer')
    }
    console.log(response);
}
</script>

<template>
    <form @submit.prevent="handleSubmitForm">
        <div>
            <div>
                <input type="text" v-model="formData.title" name="title" placeholder="Titre de l'article"
                    v-on:keyup="onGenerateSlug" required>
            </div>
            <div>
                <input type="text" v-model="formData.slug" name="slug" placeholder="Slug de l'article" required>
            </div>
            <div>
                <textarea name="content" required v-model="formData.content" placeholder="Contenu de l'article"
                    rows="10"></textarea>
            </div>
            <div>
                <p>Prévisualisation :</p>
                <p>Titre : {{ formData.title }}</p>
                <p>Slug : {{ formData.slug }}</p>
                <p>Contenu : {{ formData.content }}</p>
                <button type="submit">Envoyer</button>
            </div>
        </div>
    </form>
</template>