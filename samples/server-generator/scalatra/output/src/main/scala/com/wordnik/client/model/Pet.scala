package com.wordnik.client.model

import com.wordnik.client.model.Category
import com.wordnik.client.model.Tag
import scala.reflect.BeanProperty

case class Pet (
  id: Long,
  tags: java.util.List[Tag],
  category: Category,
  /* pet status in the store */
  status: String,
  name: String,
  photoUrls: java.util.List[String])

