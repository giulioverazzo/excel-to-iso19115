root = {
  "main" : '''<?xml version="1.0" encoding="UTF-8"?>
  <mdb:MD_Metadata xmlns:mdb="http://standards.iso.org/iso/19115/-3/mdb/2.0"
                 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                 xmlns:cat="http://standards.iso.org/iso/19115/-3/cat/1.0"
                 xmlns:gfc="http://standards.iso.org/iso/19110/gfc/1.1"
                 xmlns:cit="http://standards.iso.org/iso/19115/-3/cit/2.0"
                 xmlns:gcx="http://standards.iso.org/iso/19115/-3/gcx/1.0"
                 xmlns:gex="http://standards.iso.org/iso/19115/-3/gex/1.0"
                 xmlns:lan="http://standards.iso.org/iso/19115/-3/lan/1.0"
                 xmlns:srv="http://standards.iso.org/iso/19115/-3/srv/2.1"
                 xmlns:mas="http://standards.iso.org/iso/19115/-3/mas/1.0"
                 xmlns:mcc="http://standards.iso.org/iso/19115/-3/mcc/1.0"
                 xmlns:mco="http://standards.iso.org/iso/19115/-3/mco/1.0"
                 xmlns:mda="http://standards.iso.org/iso/19115/-3/mda/1.0"
                 xmlns:mds="http://standards.iso.org/iso/19115/-3/mds/2.0"
                 xmlns:mdt="http://standards.iso.org/iso/19115/-3/mdt/2.0"
                 xmlns:mex="http://standards.iso.org/iso/19115/-3/mex/1.0"
                 xmlns:mmi="http://standards.iso.org/iso/19115/-3/mmi/1.0"
                 xmlns:mpc="http://standards.iso.org/iso/19115/-3/mpc/1.0"
                 xmlns:mrc="http://standards.iso.org/iso/19115/-3/mrc/2.0"
                 xmlns:mrd="http://standards.iso.org/iso/19115/-3/mrd/1.0"
                 xmlns:mri="http://standards.iso.org/iso/19115/-3/mri/1.0"
                 xmlns:mrl="http://standards.iso.org/iso/19115/-3/mrl/2.0"
                 xmlns:mrs="http://standards.iso.org/iso/19115/-3/mrs/1.0"
                 xmlns:msr="http://standards.iso.org/iso/19115/-3/msr/2.0"
                 xmlns:mdq="http://standards.iso.org/iso/19157/-2/mdq/1.0"
                 xmlns:mac="http://standards.iso.org/iso/19115/-3/mac/2.0"
                 xmlns:gco="http://standards.iso.org/iso/19115/-3/gco/1.0"
                 xmlns:gml="http://www.opengis.net/gml/3.2"
                 xmlns:xlink="http://www.w3.org/1999/xlink"
                 xsi:schemaLocation="http://standards.iso.org/iso/19115/-3/mds/2.0 http://standards.iso.org/iso/19115/-3/mds/2.0/mds.xsd">
  <mdb:defaultLocale xmlns:geonet="http://www.fao.org/geonetwork">
      <lan:PT_Locale id="EN">
         <lan:language>
            <lan:LanguageCode codeList="http://www.loc.gov/standards/iso639-2/" codeListValue="eng"/>
         </lan:language>
         <lan:characterEncoding>
            <lan:MD_CharacterSetCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_CharacterSetCode"
                                     codeListValue="utf8"/>
         </lan:characterEncoding>
      </lan:PT_Locale>
  </mdb:defaultLocale>
  <mdb:metadataScope xmlns:geonet="http://www.fao.org/geonetwork">
      <mdb:MD_MetadataScope>
         <mdb:resourceScope>
            <mcc:MD_ScopeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_ScopeCode"
                              codeListValue="dataset"/>
         </mdb:resourceScope>
      </mdb:MD_MetadataScope>
  </mdb:metadataScope>
  <mdb:metadataStandard xmlns:geonet="http://www.fao.org/geonetwork">
      <cit:CI_Citation>
         <cit:title>
            <gco:CharacterString>ISO 19115-3</gco:CharacterString>
         </cit:title>
      </cit:CI_Citation>
  </mdb:metadataStandard>
  <mdb:referenceSystemInfo xmlns:geonet="http://www.fao.org/geonetwork">
      <mrs:MD_ReferenceSystem>
         <mrs:referenceSystemIdentifier>
            <mcc:MD_Identifier>
               <mcc:code>
                  <gcx:Anchor>WGS84</gcx:Anchor>
               </mcc:code>
            </mcc:MD_Identifier>
         </mrs:referenceSystemIdentifier>
      </mrs:MD_ReferenceSystem>
  </mdb:referenceSystemInfo>
    <mdb:dataQualityInfo xmlns:geonet="http://www.fao.org/geonetwork">
      <mdq:DQ_DataQuality>
         <mdq:scope>
            <mcc:MD_Scope>
               <mcc:level>
                  <mcc:MD_ScopeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_ScopeCode"
                                    codeListValue="dataset"/>
               </mcc:level>
            </mcc:MD_Scope>
         </mdq:scope>
         <mdq:report>
            <mdq:DQ_DomainConsistency>
               <mdq:result>
                  <mdq:DQ_ConformanceResult>
                     <mdq:specification>
                        <cit:CI_Citation>
                           <cit:title>
                              <gcx:Anchor>COMMISSION REGULATION (EU) No 1089/2010 of 23 November 2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards interoperability of spatial data sets and services</gcx:Anchor>
                           </cit:title>
                           <cit:date>
                              <cit:CI_Date>
                                 <cit:date>
                                    <gco:Date>2010-12-08</gco:Date>
                                 </cit:date>
                                 <cit:dateType>
                                    <cit:CI_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_DateTypeCode"
                                                         codeListValue="publication"/>
                                 </cit:dateType>
                              </cit:CI_Date>
                           </cit:date>
                        </cit:CI_Citation>
                     </mdq:specification>
                     <mdq:explanation>
                        <gco:CharacterString>This data set is conformant with the INSPIRE Implementing Rules for the interoperability of spatial data sets and services</gco:CharacterString>
                     </mdq:explanation>
                     <mdq:pass>
                        <gco:Boolean>true</gco:Boolean>
                     </mdq:pass>
                  </mdq:DQ_ConformanceResult>
               </mdq:result>
            </mdq:DQ_DomainConsistency>
         </mdq:report>
      </mdq:DQ_DataQuality>
  </mdb:dataQualityInfo>
   <mdb:contact xmlns:geonet="http://www.fao.org/geonetwork">
      <cit:CI_Responsibility>
         <cit:role>
            <cit:CI_RoleCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_RoleCode"
                             codeListValue="pointOfContact"/>
         </cit:role>
         <cit:party>
            <cit:CI_Organisation>
               <cit:name>
                  <gco:CharacterString>ISP-CNR</gco:CharacterString>
               </cit:name>
               <cit:contactInfo>
                  <cit:CI_Contact>
                     <cit:address>
                        <cit:CI_Address>
                           <cit:electronicMailAddress>
                              <gco:CharacterString>g.verazzo@isac.cnr.it</gco:CharacterString>
                           </cit:electronicMailAddress>
                        </cit:CI_Address>
                     </cit:address>
                  </cit:CI_Contact>
               </cit:contactInfo>
               <cit:individual>
                  <cit:CI_Individual>
                     <cit:name>
                        <gco:CharacterString>Giulio Verazzo</gco:CharacterString>
                     </cit:name>
                  </cit:CI_Individual>
               </cit:individual>
            </cit:CI_Organisation>
         </cit:party>
      </cit:CI_Responsibility>
  </mdb:contact>
  {0}
  </mdb:MD_Metadata>'''
}

dates = {
  "revision" : '''<mdb:dateInfo>
      <cit:CI_Date>
         <cit:date>
            <gco:DateTime>{0}</gco:DateTime>
         </cit:date>
         <cit:dateType>
            <cit:CI_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_DateTypeCode"
                                 codeListValue="revision"/>
         </cit:dateType>
      </cit:CI_Date>
  </mdb:dateInfo>''',
  "creation" : '''<mdb:dateInfo xmlns:geonet="http://www.fao.org/geonetwork">
      <cit:CI_Date>
         <cit:date>
            <gco:Date>{0}</gco:Date>
         </cit:date>
         <cit:dateType>
            <cit:CI_DateTypeCode codeList="https://standards.iso.org/iso/19115/resources/Codelists/cat/codelists.xml#CI_DateTypeCode"
                                 codeListValue="creation">creation</cit:CI_DateTypeCode>
         </cit:dateType>
      </cit:CI_Date>
  </mdb:dateInfo>'''
}

metadata_id = {
  "identifier": '''  <mdb:metadataIdentifier>
      <mcc:MD_Identifier>
         <mcc:code>
            <gco:CharacterString>{0}</gco:CharacterString>
         </mcc:code>
         <mcc:codeSpace>
            <gco:CharacterString>urn:uuid</gco:CharacterString>
         </mcc:codeSpace>
      </mcc:MD_Identifier>
  </mdb:metadataIdentifier>''',
  "linkage": '''  <mdb:metadataLinkage xmlns:geonet="http://www.fao.org/geonetwork">
      <cit:CI_OnlineResource>
         <cit:linkage>
            <gco:CharacterString>https://nadc-isp.cnr.it/srv/api/records/{0}</gco:CharacterString>
         </cit:linkage>
         <cit:function>
            <cit:CI_OnLineFunctionCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_OnLineFunctionCode"
                                       codeListValue="completeMetadata"/>
         </cit:function>
      </cit:CI_OnlineResource>
  </mdb:metadataLinkage>''' 
}

resource_lineage = {
  "main": '''<mdb:resourceLineage xmlns:geonet="http://www.fao.org/geonetwork">
      <mrl:LI_Lineage>
         <mrl:statement>
            <gco:CharacterString>{0}</gco:CharacterString>
         </mrl:statement>
         <mrl:scope>
            <mcc:MD_Scope>
               <mcc:level>
                  <mcc:MD_ScopeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_ScopeCode"
                                    codeListValue="dataset"/>
               </mcc:level>
            </mcc:MD_Scope>
         </mrl:scope>
      </mrl:LI_Lineage>
  </mdb:resourceLineage>'''
}

distribution_info = {
  "main": '''  <mdb:distributionInfo xmlns:geonet="http://www.fao.org/geonetwork">
      <mrd:MD_Distribution>
         <mrd:distributionFormat>
            <mrd:MD_Format>
               <mrd:formatSpecificationCitation>
                  <cit:CI_Citation>
                     <cit:title>
                        <gco:CharacterString>{0}</gco:CharacterString>
                     </cit:title>
                     <cit:edition>
                        <gco:CharacterString>1</gco:CharacterString>
                     </cit:edition>
                  </cit:CI_Citation>
               </mrd:formatSpecificationCitation>
            </mrd:MD_Format>
         </mrd:distributionFormat>
         {1}
      </mrd:MD_Distribution>
  </mdb:distributionInfo>''',
  "transfer_option":'''<mrd:transferOptions>
            <mrd:MD_DigitalTransferOptions>
               <mrd:onLine>
                  <cit:CI_OnlineResource>
                     <cit:linkage>
                        <gco:CharacterString>{0}</gco:CharacterString>
                     </cit:linkage>
                     <cit:protocol>
                        <gco:CharacterString>WWW:LINK-1.0-http--link</gco:CharacterString>
                     </cit:protocol>
                     <cit:name>
                        <gco:CharacterString>Data resource</gco:CharacterString>
                     </cit:name>
                     <cit:description>
                        <gco:CharacterString>Link to external resource</gco:CharacterString>
                     </cit:description>
                     <cit:function>
                        <cit:CI_OnLineFunctionCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_OnLineFunctionCode"
                                                   codeListValue="information"/>
                     </cit:function>
                  </cit:CI_OnlineResource>
               </mrd:onLine>
            </mrd:MD_DigitalTransferOptions>
         </mrd:transferOptions>'''
}

identification_info = {
  "main" : '''<mdb:identificationInfo xmlns:geonet="http://www.fao.org/geonetwork">
      <mri:MD_DataIdentification>
         <mri:citation>
            <cit:CI_Citation>
               <cit:title>
                  <gco:CharacterString>{0}</gco:CharacterString>
               </cit:title>
               <cit:identifier>
                  <mcc:MD_Identifier>
                     <mcc:code>
                        <gcx:Anchor xlink:href="https://nadc-isp.cnr.it/srv/api/records/{1}">https://nadc-isp.cnr.it/srv/api/records/{1}</gcx:Anchor>
                     </mcc:code>
                  </mcc:MD_Identifier>
               </cit:identifier>
               <cit:identifier/>
            </cit:CI_Citation>
         </mri:citation>
         <mri:abstract>
            <gco:CharacterString>{2}</gco:CharacterString>
         </mri:abstract>
         <mri:status>
            <mcc:MD_ProgressCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_ProgressCode"
                                 codeListValue="{3}"/>
         </mri:status>

         <!-- persons -->
         {4}

         <mri:spatialRepresentationType>
            <mcc:MD_SpatialRepresentationTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_SpatialRepresentationTypeCode"
                                                  codeListValue="textTable"/>
         </mri:spatialRepresentationType>
         <mri:spatialResolution>
            <mri:MD_Resolution>
               <mri:equivalentScale>
                  <mri:MD_RepresentativeFraction>
                     <mri:denominator>
                        <gco:Integer>1</gco:Integer>
                     </mri:denominator>
                  </mri:MD_RepresentativeFraction>
               </mri:equivalentScale>
            </mri:MD_Resolution>
         </mri:spatialResolution>
         <mri:topicCategory>
            <mri:MD_TopicCategoryCode>{5}</mri:MD_TopicCategoryCode>
         </mri:topicCategory>

         <!-- Keywords -->
         {6}

         <mri:resourceConstraints>
            <mco:MD_LegalConstraints>
               <mco:useConstraints>
                  <mco:MD_RestrictionCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_RestrictionCode"
                                          codeListValue="license"/>
               </mco:useConstraints>
               <mco:otherConstraints>
                  <gcx:Anchor xlink:href="https://creativecommons.org/licenses/by-nc-sa/4.0/">{7}</gcx:Anchor>
               </mco:otherConstraints>
            </mco:MD_LegalConstraints>
         </mri:resourceConstraints>
         <mri:associatedResource>
            <mri:MD_AssociatedResource>
               <mri:name>
                  <cit:CI_Citation>
                     <cit:title>
                        <gco:CharacterString>PNRA</gco:CharacterString>
                     </cit:title>
                     <cit:identifier>
                        <mcc:MD_Identifier>
                           <mcc:code>
                              <gcx:Anchor xlink:href="https://www.pnra.aq/">{8}</gcx:Anchor>
                           </mcc:code>
                        </mcc:MD_Identifier>
                     </cit:identifier>
                  </cit:CI_Citation>
               </mri:name>
               <mri:associationType>
                  <mri:DS_AssociationTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#DS_AssociationTypeCode"
                                              codeListValue="dependency"/>
               </mri:associationType>
               <mri:initiativeType>
                  <mri:DS_InitiativeTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#DS_InitiativeTypeCode"
                                             codeListValue="project"/>
               </mri:initiativeType>
            </mri:MD_AssociatedResource>
         </mri:associatedResource>
         <mri:defaultLocale>
            <lan:PT_Locale>
               <lan:language>
                  <lan:LanguageCode codeList="http://www.loc.gov/standards/iso639-2/" codeListValue="eng"/>
               </lan:language>
               <lan:characterEncoding>
                  <lan:MD_CharacterSetCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_CharacterSetCode"
                                           codeListValue="utf8"/>
               </lan:characterEncoding>
            </lan:PT_Locale>
         </mri:defaultLocale>
      </mri:MD_DataIdentification>
  </mdb:identificationInfo>''',
  "person":'''<mri:pointOfContact>
            <cit:CI_Responsibility>
               <cit:role>
                  <cit:CI_RoleCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_RoleCode"
                                   codeListValue="{0}"/>
               </cit:role>
               <cit:party>
                  <cit:CI_Organisation>
                     <cit:name>
                        <gco:CharacterString>{1}</gco:CharacterString>
                     </cit:name>
                     <cit:contactInfo>
                        <cit:CI_Contact>
                           <cit:address>
                              <cit:CI_Address>
                                 <cit:electronicMailAddress>
                                    <gco:CharacterString>{2}</gco:CharacterString>
                                 </cit:electronicMailAddress>
                              </cit:CI_Address>
                           </cit:address>
                        </cit:CI_Contact>
                     </cit:contactInfo>
                     <cit:individual>
                        <cit:CI_Individual>
                           <cit:name>
                              <gco:CharacterString>{3}</gco:CharacterString>
                           </cit:name>
                           <cit:positionName>
                              <gco:CharacterString>Researcher</gco:CharacterString>
                           </cit:positionName>
                        </cit:CI_Individual>
                     </cit:individual>
                  </cit:CI_Organisation>
               </cit:party>
            </cit:CI_Responsibility>
         </mri:pointOfContact>'''
}

kw_templates = {
  "inspire": '''<mri:descriptiveKeywords>
            <mri:MD_Keywords>
               <mri:keyword>
                  <gcx:Anchor xlink:href="http://inspire.ec.europa.eu/theme/ac">Atmospheric conditions</gcx:Anchor>
               </mri:keyword>
               <mri:type>
                  <mri:MD_KeywordTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_KeywordTypeCode"
                                          codeListValue="theme"/>
               </mri:type>
               <mri:thesaurusName>
                  <cit:CI_Citation>
                     <cit:title>
                        <gcx:Anchor xlink:href="http://inspire.ec.europa.eu/theme#">GEMET - INSPIRE themes, version 1.0</gcx:Anchor>
                     </cit:title>
                     <cit:date>
                        <cit:CI_Date>
                           <cit:date>
                              <gco:Date>2008-06-01</gco:Date>
                           </cit:date>
                           <cit:dateType>
                              <cit:CI_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_DateTypeCode"
                                                   codeListValue="publication"/>
                           </cit:dateType>
                        </cit:CI_Date>
                     </cit:date>
                     <cit:identifier>
                        <mcc:MD_Identifier>
                           <mcc:code>
                              <gcx:Anchor xlink:href="https://nadc-isp.cnr.it/srv/eng/thesaurus.download?ref=external.theme.httpinspireeceuropaeutheme-theme">geonetwork.thesaurus.external.theme.httpinspireeceuropaeutheme-theme</gcx:Anchor>
                           </mcc:code>
                        </mcc:MD_Identifier>
                     </cit:identifier>
                  </cit:CI_Citation>
               </mri:thesaurusName>
            </mri:MD_Keywords>
         </mri:descriptiveKeywords>''',
  "instruments" : '''<mri:descriptiveKeywords>
            <mri:MD_Keywords>
               <mri:keyword>
                  <gco:CharacterString>RADIOMETERS</gco:CharacterString>
               </mri:keyword>
               <mri:type>
                  <mri:MD_KeywordTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_KeywordTypeCode"
                                          codeListValue="theme"/>
               </mri:type>
               <mri:thesaurusName>
                  <cit:CI_Citation>
                     <cit:title>
                        <gcx:Anchor xlink:href="https://gcmdservices.gsfc.nasa.gov/kms/concepts/concept_scheme/instruments#">GCMD - Instruments</gcx:Anchor>
                     </cit:title>
                     <cit:date>
                        <cit:CI_Date>
                           <cit:date>
                              <gco:Date>2020-06-22</gco:Date>
                           </cit:date>
                           <cit:dateType>
                              <cit:CI_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_DateTypeCode"
                                                   codeListValue="publication"/>
                           </cit:dateType>
                        </cit:CI_Date>
                     </cit:date>
                     <cit:identifier>
                        <mcc:MD_Identifier>
                           <mcc:code>
                              <gcx:Anchor xlink:href="https://nadc-isp.cnr.it/srv/eng/thesaurus.download?ref=external.theme.gcmd-instruments">geonetwork.thesaurus.external.theme.gcmd-instruments</gcx:Anchor>
                           </mcc:code>
                        </mcc:MD_Identifier>
                     </cit:identifier>
                  </cit:CI_Citation>
               </mri:thesaurusName>
            </mri:MD_Keywords>
         </mri:descriptiveKeywords>''',
  "locations":'''<mri:descriptiveKeywords>
            <mri:MD_Keywords>
               <mri:keyword>
                  <gco:CharacterString>ANTARCTICA</gco:CharacterString>
               </mri:keyword>
               <mri:type>
                  <mri:MD_KeywordTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_KeywordTypeCode"
                                          codeListValue="theme"/>
               </mri:type>
               <mri:thesaurusName>
                  <cit:CI_Citation>
                     <cit:title>
                        <gcx:Anchor xlink:href="https://gcmdservices.gsfc.nasa.gov/kms/concepts/concept_scheme/locations#">GCMD - Locations</gcx:Anchor>
                     </cit:title>
                     <cit:date>
                        <cit:CI_Date>
                           <cit:date>
                              <gco:Date>2020-06-22</gco:Date>
                           </cit:date>
                           <cit:dateType>
                              <cit:CI_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_DateTypeCode"
                                                   codeListValue="publication"/>
                           </cit:dateType>
                        </cit:CI_Date>
                     </cit:date>
                     <cit:identifier>
                        <mcc:MD_Identifier>
                           <mcc:code>
                              <gcx:Anchor xlink:href="https://nadc-isp.cnr.it/srv/eng/thesaurus.download?ref=external.theme.gcmd-locations">geonetwork.thesaurus.external.theme.gcmd-locations</gcx:Anchor>
                           </mcc:code>
                        </mcc:MD_Identifier>
                     </cit:identifier>
                  </cit:CI_Citation>
               </mri:thesaurusName>
            </mri:MD_Keywords>
         </mri:descriptiveKeywords>''',
  "platforms":'''<mri:descriptiveKeywords>
            <mri:MD_Keywords>
               <mri:keyword>
                  <gco:CharacterString>GROUND-BASED OBSERVATIONS</gco:CharacterString>
               </mri:keyword>
               <mri:keyword>
                  <gco:CharacterString>GROUND STATIONS</gco:CharacterString>
               </mri:keyword>
               <mri:type>
                  <mri:MD_KeywordTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_KeywordTypeCode"
                                          codeListValue="theme"/>
               </mri:type>
               <mri:thesaurusName>
                  <cit:CI_Citation>
                     <cit:title>
                        <gcx:Anchor xlink:href="https://gcmdservices.gsfc.nasa.gov/kms/concepts/concept_scheme/platforms#">GCMD - Platforms</gcx:Anchor>
                     </cit:title>
                     <cit:date>
                        <cit:CI_Date>
                           <cit:date>
                              <gco:Date>2020-06-22</gco:Date>
                           </cit:date>
                           <cit:dateType>
                              <cit:CI_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_DateTypeCode"
                                                   codeListValue="publication"/>
                           </cit:dateType>
                        </cit:CI_Date>
                     </cit:date>
                     <cit:identifier>
                        <mcc:MD_Identifier>
                           <mcc:code>
                              <gcx:Anchor xlink:href="https://nadc-isp.cnr.it/srv/eng/thesaurus.download?ref=external.theme.gcmd-platforms">geonetwork.thesaurus.external.theme.gcmd-platforms</gcx:Anchor>
                           </mcc:code>
                        </mcc:MD_Identifier>
                     </cit:identifier>
                  </cit:CI_Citation>
               </mri:thesaurusName>
            </mri:MD_Keywords>
         </mri:descriptiveKeywords>''',
  "sciencekeywords":'''<mri:descriptiveKeywords>
            <mri:MD_Keywords>
               <mri:keyword>
                  <gco:CharacterString>IRRADIANCE</gco:CharacterString>
               </mri:keyword>
               <mri:keyword>
                  <gco:CharacterString>SOLAR IRRADIANCE</gco:CharacterString>
               </mri:keyword>
               <mri:type>
                  <mri:MD_KeywordTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_KeywordTypeCode"
                                          codeListValue="theme"/>
               </mri:type>
               <mri:thesaurusName>
                  <cit:CI_Citation>
                     <cit:title>
                        <gcx:Anchor xlink:href="https://gcmdservices.gsfc.nasa.gov/kms/concepts/concept_scheme/sciencekeywords#">GCMD - Science Keywords</gcx:Anchor>
                     </cit:title>
                     <cit:date>
                        <cit:CI_Date>
                           <cit:date>
                              <gco:Date>2015-07-17</gco:Date>
                           </cit:date>
                           <cit:dateType>
                              <cit:CI_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_DateTypeCode"
                                                   codeListValue="publication"/>
                           </cit:dateType>
                        </cit:CI_Date>
                     </cit:date>
                     <cit:identifier>
                        <mcc:MD_Identifier>
                           <mcc:code>
                              <gcx:Anchor xlink:href="https://nadc-isp.cnr.it/srv/eng/thesaurus.download?ref=external.theme.gcmd-sciencekeywords">geonetwork.thesaurus.external.theme.gcmd-sciencekeywords</gcx:Anchor>
                           </mcc:code>
                        </mcc:MD_Identifier>
                     </cit:identifier>
                  </cit:CI_Citation>
               </mri:thesaurusName>
            </mri:MD_Keywords>
         </mri:descriptiveKeywords>''',       
  "providers":'''<mri:descriptiveKeywords>
            <mri:MD_Keywords>
               <mri:keyword>
                  <gco:CharacterString>IT/PNRA</gco:CharacterString>
               </mri:keyword>
               <mri:type>
                  <mri:MD_KeywordTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_KeywordTypeCode"
                                          codeListValue="theme"/>
               </mri:type>
               <mri:thesaurusName>
                  <cit:CI_Citation>
                     <cit:title>
                        <gcx:Anchor xlink:href="https://gcmdservices.gsfc.nasa.gov/kms/concepts/concept_scheme/providers#">GCMD - Providers</gcx:Anchor>
                     </cit:title>
                     <cit:date>
                        <cit:CI_Date>
                           <cit:date>
                              <gco:Date>2020-06-22</gco:Date>
                           </cit:date>
                           <cit:dateType>
                              <cit:CI_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_DateTypeCode"
                                                   codeListValue="publication"/>
                           </cit:dateType>
                        </cit:CI_Date>
                     </cit:date>
                     <cit:identifier>
                        <mcc:MD_Identifier>
                           <mcc:code>
                              <gcx:Anchor xlink:href="https://nadc-isp.cnr.it/srv/eng/thesaurus.download?ref=external.theme.gcmd-providers">geonetwork.thesaurus.external.theme.gcmd-providers</gcx:Anchor>
                           </mcc:code>
                        </mcc:MD_Identifier>
                     </cit:identifier>
                  </cit:CI_Citation>
               </mri:thesaurusName>
            </mri:MD_Keywords>
         </mri:descriptiveKeywords>''',
  "chronounits": '''<mri:descriptiveKeywords>
            <mri:MD_Keywords>
               <mri:keyword>
                  <gco:CharacterString>EARLY</gco:CharacterString>
               </mri:keyword>
               <mri:type>
                  <mri:MD_KeywordTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_KeywordTypeCode"
                                          codeListValue="temporal"/>
               </mri:type>
               <mri:thesaurusName>
                  <cit:CI_Citation>
                     <cit:title>
                        <gcx:Anchor xlink:href="https://gcmdservices.gsfc.nasa.gov/kms/concepts/concept_scheme/chrono_units#">GCMD - Chrono units</gcx:Anchor>
                     </cit:title>
                     <cit:date>
                        <cit:CI_Date>
                           <cit:date>
                              <gco:Date>2020-06-19</gco:Date>
                           </cit:date>
                           <cit:dateType>
                              <cit:CI_DateTypeCode codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_DateTypeCode"
                                                   codeListValue="publication"/>
                           </cit:dateType>
                        </cit:CI_Date>
                     </cit:date>
                     <cit:identifier>
                        <mcc:MD_Identifier>
                           <mcc:code>
                              <gcx:Anchor xlink:href="https://nadc-isp.cnr.it/srv/eng/thesaurus.download?ref=external.temporal.gcmd-chrono-units">geonetwork.thesaurus.external.temporal.gcmd-chrono-units</gcx:Anchor>
                           </mcc:code>
                        </mcc:MD_Identifier>
                     </cit:identifier>
                  </cit:CI_Citation>
               </mri:thesaurusName>
            </mri:MD_Keywords>
         </mri:descriptiveKeywords>'''
} 