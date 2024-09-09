<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                exclude-result-prefixes="">

  <xsl:template match="/">
    <elements>
      <xsl:apply-templates select="//desc[@objtype='function']"/>
      <xsl:apply-templates select="//desc[@objtype='attribute' or @objtype='class']"/>
      <xsl:apply-templates select="//desc[@objtype='data']"/>
    </elements>
  </xsl:template>

  <xsl:template match="desc[@objtype='attribute' or @objtype='class' or @objtype='data']">
    <element>
      <kind>
        <xsl:choose>
          <xsl:when test="@objtype='attribute' or @objtype='class'">type</xsl:when>
          <xsl:when test="@objtype='data'">constant</xsl:when>
        </xsl:choose>
      </kind>
      <name>
        <xsl:value-of select="desc_signature/desc_name"/>
      </name>
      <type>
        <xsl:value-of select="substring(normalize-space(desc_signature/desc_annotation), 3)"/>
      </type>
      <description>
        <xsl:apply-templates select="desc_content/paragraph"/>
      </description>
    </element>
  </xsl:template>

  <xsl:template match="desc[@objtype='function']">
    <element>
      <kind>function</kind>
      <name>
        <xsl:value-of select="desc_signature/desc_name"/>
      </name>
      <description>
        <xsl:apply-templates select="desc_content/paragraph[position() > 0]"/>
        <xsl:apply-templates select="desc_content/figure"/>
      </description>
      <parameters>
        <xsl:apply-templates select="desc_signature/desc_parameterlist/desc_parameter"/>
      </parameters>
      <xsl:if test="desc_signature/desc_returns">
        <returnValue>
          <type>
            <xsl:value-of select="desc_signature/desc_returns"/>
          </type>
          <description>
            <xsl:value-of select="normalize-space(desc_content/field_list/field[field_name='Returns']/field_body/paragraph)"/>
          </description>
        </returnValue>
      </xsl:if>
      <xsl:if test="contains(desc_signature/@module, '.io')">
        <sideEffects>true</sideEffects>
      </xsl:if>
    </element>
  </xsl:template>

  <xsl:template match="desc_parameter">
    <parameter>
      <name>
        <xsl:value-of select="desc_sig_name[1]"/>
      </name>
      <type>
        <xsl:for-each select="desc_sig_name[position() > 1]">
          <xsl:value-of select="."/>
        </xsl:for-each>
      </type>
      <xsl:if test="inline">
        <default>
          <xsl:value-of select="inline"/>
        </default>
      </xsl:if>
      <description>
        <xsl:value-of select="normalize-space(substring-after(../../../desc_content/field_list/field[field_name='Parameters']/field_body//paragraph[literal_strong = current()/desc_sig_name[1]], concat(current()/desc_sig_name[1],' – ')))"/>
      </description>
    </parameter>
  </xsl:template>

  <xsl:template match="//paragraph">
    <p>
      <xsl:value-of select="normalize-space(.)"/>
    </p>
  </xsl:template>
  
  <xsl:template match="figure">
    <figure>
      <url>
        <xsl:value-of select="image/@uri"/>
      </url>
      <caption>
        <xsl:value-of select="caption"/>
      </caption>
    </figure>
  </xsl:template>

</xsl:stylesheet>
